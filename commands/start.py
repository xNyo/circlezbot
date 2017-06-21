from utils import sentry
from utils import text
from singletons.bot import Bot

bot = Bot()


@bot.command("start")
@sentry.capture
async def start(chat, match):
    await chat.send_text(text.START, parse_mode="markdown")
