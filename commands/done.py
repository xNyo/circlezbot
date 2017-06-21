import json

from aiotg import Chat
from emoji import emojize

from singletons.bot import Bot
from singletons.config import Config
from utils import sentry
from utils import text

bot = Bot()


@bot.callback
@sentry.capture
async def done(chat, cq):
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
