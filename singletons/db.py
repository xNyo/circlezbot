import aiomysql
import logging
from aiomysql import create_pool

from utils.singleton import singleton


@singleton
class Db:
    _logger = logging.getLogger(__name__)

    @classmethod
    async def create(cls, host, port, username, password, database=None, maxsize=0, loop=None):
        """
        Creates a db util object.
        This function is a coroutine.

        :param host: MySQL host
        :param port: MySQL port
        :param username: MySQL username
        :param password: MySQL password
        :param database: MySQL database name
        :param maxsize: max connections in pool
        :param loop: IOLoop object
        :return:
        """
        self = Db()
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.maxsize = maxsize
        self.minsize = 0 if self.maxsize == 0 else 1
        self._logger.debug("Created MySQL pool ({}@{}:{}), size {} - {}".format(
            self.username, self.host, self.database, self.minsize, self.maxsize
        ))
        self.pool = await create_pool(maxsize=self.maxsize,
                                      minsize=self.minsize,
                                      host=self.host,
                                      port=self.port,
                                      user=self.username,
                                      password=self.password,
                                      db=self.database,
                                      autocommit=True,
                                      loop=loop)
        return self

    async def fetch(self, query, params=None, _all=False):
        """
        Fetches a single value from db.
        This function is a coroutine.

        :param query: query string
        :param params: list containing parameters. optional.
        :param _all: if True, fetch all results. Used internally, use `fetchall` instead.
        :return: `None` if the query returned no results, `dict` if the query returned something
        """
        if params is None:
            params = []

        async with self.pool.acquire() as conn:
            try:
                async with conn.cursor(aiomysql.DictCursor) as cur:
                    try:
                        self._logger.log(5, query)
                        await cur.execute(query, params)
                        if _all:
                            value = await cur.fetchall()
                        else:
                            value = await cur.fetchone()
                        return value
                    finally:
                        await cur.close()
            finally:
                conn.close()

    async def fetch_all(self, query, params=None):
        """
        Run a query and fetch all results.
        This function is a coroutine.

        :param query: query string
        :param params: list containing params. Optional.
        :return: `None` if the query returned no results, list of `dict`s if the query returned something
        """
        result = await self.fetch(query, params, True)
        return result

    async def execute(self, query, params=None):
        """
        Execute one or more sql statements.
        This function is a coroutine

        :param query: query string
        :param params: list containing params. Optional.
        :return: int with last row id if the query was an `UPDATE` or `INSERT`. `None` instead.
        """
        if params is None:
            params = []
        async with self.pool.acquire() as conn:
            try:
                async with conn.cursor() as cur:
                    try:
                        self._logger.log(5, query)
                        await cur.execute(query, params)
                        result = cur.lastrowid
                    finally:
                        await cur.close()
            finally:
                conn.close()
        return result
