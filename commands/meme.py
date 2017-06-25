from utils import sentry
from singletons.bot import Bot

bot = Bot()


@bot.command("hime")
@sentry.capture
async def start(chat, match):
    await chat.send_text("Hime hime suki suki daisuki")
