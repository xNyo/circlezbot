import asyncio

from raven.transport import ThreadedHTTPTransport

from singletons.bot import Bot
from singletons.config import Config
from singletons.db import Db
from singletons.sentry import SentryClient


def main():
    # Read config
    conf = Config().config

    # Connect to MySQL
    asyncio.get_event_loop().run_until_complete(
        Db().create(
            host=conf["DB_HOST"],
            port=conf["DB_PORT"],
            username=conf["DB_USERNAME"],
            password=conf["DB_PASSWORD"],
            database=conf["DB_DATABASE"],
            maxsize=conf["DB_POOL_SIZE"]
        )
    )

    # Initialize sentry
    if Config().config["SENTRY_DSN"] != "":
        SentryClient(
            conf["SENTRY_DSN"],
            enable_breadcrumbs=True,
            transport=ThreadedHTTPTransport,
            string_max_length=8192)
    else:
        print("Sentry logging disabled")

    # Initialize bot
    bot = Bot(conf["TELEGRAM_API_TOKEN"])

    from commands import start
    from commands import referral

    print("Click da circlez")
    bot.run()


if __name__ == "__main__":
    main()
