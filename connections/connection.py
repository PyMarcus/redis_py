from redis import Redis
from .settings import connections


class ConnectionHandle:
    def __init__(self) -> None:
        self.__host = connections['HOST']
        self.__port = connections['PORT']
        self.__db = connections['DB']
        self.__connection = None

    def __connect(self) -> None:
        self.__connection = Redis(
            host=self.__host,
            port=self.__port,
            db=self.__db
        )

    def get_conn(self) -> Redis:
        self.__connect()
        return self.__connection
