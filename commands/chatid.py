from utils import sentry
from singletons.bot import Bot

bot = Bot()


@bot.command("chatid")
@sentry.capture
async def start(chat, match):
    await chat.send_text("`{}`".format(chat.sender["id"]), parse_mode="markdown")
