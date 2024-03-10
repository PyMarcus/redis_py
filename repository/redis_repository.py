from redis import Redis
from typing import Any


class RedisRepository:
    def __init__(self, redis_conn: Redis) -> None:
        self.__redis_conn = redis_conn

    def insert(self, key: str, value: Any) -> None:
        self.__redis_conn.set(key, value)

    def h_insert(self, key: str, key_a: str, value_key_a: Any) -> None:
        self.__redis_conn.hset(key, key_a, value_key_a)

    def delete(self, key: str) -> None:
        self.__redis_conn.delete(key)

    def h_delete(self, key: str, key_a: str) -> None:
        self.__redis_conn.hdel(key, key_a)

    def update(self, key: str, value: Any) -> None:
        self.__redis_conn.set(key, value)

    def h_update(self, key: str, key_a: str, value_a: Any):
        self.__redis_conn.hset(key, key_a, value_a)

    def get_value(self, key: str) -> Any:
        return self.__redis_conn.get(key).decode("utf-8")

    def h_get_value(self, key: str, key_a: str) -> Any:
        return self.__redis_conn.hget(key, key_a).decode("utf-8")

    def h_get_all(self, key: str) -> Any:
        return self.__redis_conn.hgetall(key)
