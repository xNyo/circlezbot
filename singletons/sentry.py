from raven import Client

from utils.singleton import singleton


@singleton
class SentryClient(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
