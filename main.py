from connections import ConnectionHandle
from repository import RedisRepository


redis_conn = ConnectionHandle().get_conn()
repository = RedisRepository(redis_conn)

repository.insert("hello", "world!")
print(repository.get_value("hello"))
