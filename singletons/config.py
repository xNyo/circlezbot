from decouple import config

from utils.singleton import singleton


@singleton
class Config:
    def __init__(self):
        self.config = {
            "DB_HOST": config("DB_HOST", default="localhost"),
            "DB_PORT": config("DB_PORT", default="3306", cast=int),
            "DB_USERNAME": config("DB_USERNAME", default="root"),
            "DB_PASSWORD": config("DB_PASSWORD", default=""),
            "DB_DATABASE": config("DB_DATABASE", default="girada"),
            "DB_POOL_SIZE": config("DB_POOL_SIZE", default="8", cast=int),

            "GROUP_ID": config("GROUP_ID", default="", cast=int),

            "TELEGRAM_API_TOKEN": config("TELEGRAM_API_TOKEN", default=""),

            "SENTRY_DSN": config("SENTRY_DSN", default=""),
        }
