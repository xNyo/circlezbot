import json

import time
from aiotg import Chat
from emoji import emojize

from singletons.bot import Bot
from singletons.config import Config
from singletons.db import Db
from utils import sentry
from utils import text

bot = Bot()


@bot.callback
@sentry.capture
async def callback(chat, cq):
    if cq.data == "referral":
        # Check if we have already used this account
        ref = await Db().fetch("SELECT referrals.* FROM invited LEFT JOIN referrals "
                               "ON invited.referral_id = referrals.id WHERE invited.telegram_id = %s LIMIT 1",
                               [cq.src["from"]["id"]])

        # Remove last two lines and reply keyboard markup
        await chat.edit_text(
            cq.src["message"]["message_id"],
            "\n".join(cq.src["message"]["text"].split("\n")[:-2]).strip(),
            markup={}
        )

        # Send new message with inline query keyboard
        if ref is None:
            # New user
            await chat.send_text(text.INSTRUCTIONS_WARNING, parse_mode="markdown",
                                 reply_markup=json.dumps({
                                    "inline_keyboard": [[{
                                        "text": emojize(
                                            ":white_check_mark: Ho tutto pronto, dimmi cosa fare!", use_aliases=True
                                        ),
                                        "callback_data": "start"
                                    }], [{
                                        "text": emojize(":thinking_face: Ci devo ancora pensare..."),
                                        "callback_data": "stop"
                                    }]]
                                 }), disable_web_page_preview=True)
        else:
            # Already used
            await chat.send_text(text.ALREADY_USED, parse_mode="markdown")
    elif cq.data == "start":
        # Check if we have already used a referral
        ref = await Db().fetch("SELECT referrals.* FROM invited LEFT JOIN referrals "
                               "ON invited.referral_id = referrals.id WHERE invited.telegram_id = %s LIMIT 1",
                               [cq.src["from"]["id"]])
        if ref is None:
            # Get referral index
            referral_index = await Db().fetch("SELECT latest_referral FROM latest_referral WHERE 1 LIMIT 1")
            referral_index = referral_index["latest_referral"]

            # Increment referral index
            await Db().execute("UPDATE latest_referral SET latest_referral = (latest_referral + 1) %% "
                               "(SELECT COUNT(*) FROM referrals WHERE 1 LIMIT 1) WHERE 1 LIMIT 1")

            ref = await Db().fetch("SELECT * FROM referrals WHERE 1 LIMIT 1 OFFSET {}".format(referral_index))

            # Insert invited
            await Db().execute("INSERT INTO invited (id, telegram_id, `time`, referral_id) VALUES (NULL, %s, %s, %s)", [
                cq.src["from"]["id"],
                int(time.time()),
                ref["id"]
            ])

            # Send message to referral
            await bot.send_message(ref["telegram_id"], text.ADMIN_REFERRAL_NOTIFY.format(
                cq.src["from"]["first_name"] if "first_name" in cq.src["from"] else "Boh",
                cq.src["from"]["last_name"] if "last_name" in cq.src["from"] else "Boh",
                cq.src["from"]["username"] if "username" in cq.src["from"] else "boh",
                cq.src["from"]["id"]), parse_mode="markdown")

            # Send message
            await chat.edit_text(cq.src["message"]["message_id"], text.INSTRUCTIONS.format(code=ref["referral"]),
                                 markup={
                                    "inline_keyboard": [[{
                                        "text": emojize(":money_with_wings: Registrati e ricevi 5€ gratis"),
                                        "url": "https://www.circle.com/invite/{}".format(ref["referral"])
                                    }], [{
                                        "text": emojize(":thumbs_up: Ho ricevuto i miei 5€!"),
                                        "callback_data": "done"
                                    }]]
                                 }, parse_mode="markdown")
        else:
            # This user has already used a referral
            await chat.send_text(text.ALREADY_USED, parse_mode="markdown")
    elif cq.data == "done":
        # Make sure we have used a referral
        ref = await Db().fetch("SELECT referrals.* FROM invited LEFT JOIN referrals "
                               "ON invited.referral_id = referrals.id WHERE invited.telegram_id = %s LIMIT 1",
                               [cq.src["from"]["id"]])
        if ref is None:
            return

        # Kick from main group
        try:
            await Chat(bot, Config().config["GROUP_ID"]).kick_chat_member(cq.src["from"]["id"])
        except:
            pass

        # Bastardata
        await chat.edit_text(cq.src["message"]["message_id"], text.DONE, parse_mode="markdown", markup={
            "inline_keyboard": [[{
                "text": emojize(":mobile_phone: Sconti dell'80% su prodotti tecnologici"),
                "url": "http://t.me/giradagroupnetwork"
            }], [{
                "text": emojize(":earth_africa: Il nostro network", use_aliases=True),
                "url": "http://t.me/giaquonetwork"
            }]]
        })
    elif cq.data == "stop":
        # Make sure we have already used a referral
        ref = await Db().fetch("SELECT referrals.* FROM invited LEFT JOIN referrals "
                               "ON invited.referral_id = referrals.id WHERE invited.telegram_id = %s LIMIT 1",
                               [cq.src["from"]["id"]])
        if ref is None:
            await chat.edit_text(cq.src["message"]["message_id"], text.STOP, parse_mode="markdown")
