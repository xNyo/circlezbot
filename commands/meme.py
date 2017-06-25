import aiofiles

from utils import sentry
from singletons.bot import Bot

bot = Bot()


@bot.command("hime")
@sentry.capture
async def hime(chat, match):
    async with aiofiles.open("assets/hime.mp3", "rb") as f:
        await chat.send_audio(await f.read(), title="Hime Hime Suki Suki Daisuki")


@bot.command("haitai")
@sentry.capture
async def haitai(chat, match):
    async with aiofiles.open("assets/haitai.mp3", "rb") as f:
        await chat.send_audio(await f.read(), title="Haitai")