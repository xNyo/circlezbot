from singletons.sentry import SentryClient


def capture(f):
    async def wrapper(*args, **kwargs):
        try:
            return await f(*args, **kwargs)
        except Exception as e:
            SentryClient().captureException()
            raise
    return wrapper
