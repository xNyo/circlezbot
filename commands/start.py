import json

from emoji import emojize

from utils import sentry
from utils import text
from singletons.bot import Bot

bot = Bot()


@bot.command("start")
@sentry.capture
async def start(chat, match):
    await chat.send_text(text.START, parse_mode="markdown", reply_markup=json.dumps({
        "inline_keyboard": [[{
            "text": emojize(":money_with_wings: Cominciamo!"),
            "callback_data": "referral"
        }]]
    }))
