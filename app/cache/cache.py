import json
from fastapi.encoders import jsonable_encoder
from app.cache.redis import redisConnection


class Cache:
    TTL = 60

    def __init__(self):
        self.__connection = redisConnection

    def get_or_set(self, key, getter_function):
        item = self.__connection.get(key)

        if item is None:
            db_item = getter_function()
            item = json.dumps(jsonable_encoder(db_item))
            self.__connection.set(key, item, ex=self.TTL)

        return json.loads(item)

    def set(self, key):
        pass

    def expiry(self, key):
        pass
