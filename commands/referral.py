import time
import json
from emoji import emojize

from singletons.bot import Bot
from singletons.db import Db

from utils import sentry
from utils import text

bot = Bot()


@sentry.capture
@bot.command("referral")
async def referral(chat, match):
    # Check if we have already used a referral
    ref = await Db().fetch("SELECT referrals.* FROM invited LEFT JOIN referrals "
                           "ON invited.referral_id = referrals.id WHERE invited.telegram_id = %s LIMIT 1", [chat.sender["id"]])
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
            chat.sender["id"],
            int(time.time()),
            ref["id"]
        ])

        # Send message to referral
        await bot.send_message(ref["telegram_id"], text.ADMIN_REFERRAL_NOTIFY.format(
            chat.sender["first_name"] if "first_name" in chat.sender else "Boh",
            chat.sender["last_name"] if "last_name" in chat.sender else "Boh",
            chat.sender["username"] if "username" in chat.sender else "boh",
            chat.sender["id"]), parse_mode="markdown")

        # Send message
        await chat.send_text(text.INSTRUCTIONS.format(code=ref["referral"]), reply_markup=json.dumps({
            "inline_keyboard": [[{
                "text": emojize(":money_with_wings: Registrati e ricevi 5€ gratis"),
                "url": "https://www.circle.com/invite/{}".format(ref["referral"])
            }]]
        }), parse_mode="markdown", disable_web_page_preview=True)
    else:
        # This user has already used a referral
        await chat.send_text(text.ALREADY_USED, parse_mode="markdown")
