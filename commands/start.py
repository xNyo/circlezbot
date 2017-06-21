from utils import sentry
from utils import text
from singletons.bot import Bot

bot = Bot()


@sentry.capture
@bot.command("start")
async def start(chat, match):
    await chat.send_text(text.START, parse_mode="markdown")
