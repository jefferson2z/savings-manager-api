import json
from fastapi.encoders import jsonable_encoder
from app.cache.redis import redisConnection


class Cache:
    TTL = 60

    def __init__(self):
        self.__connection = redisConnection

    def get(self, key):
        item = self.__connection.get(key)
        if item is None:
            return None
        return json.loads(item)

    def get_or_set(self, key, getter_function):
        item = self.get(key)

        if item is None:
            db_item = getter_function()
            item = self.set(key, db_item)

        return item

    def set(self, key, data):
        item = json.dumps(jsonable_encoder(data))
        self.__connection.set(key, item, ex=self.TTL)
        return json.loads(item)

    def expiry(self, key):
        self.__connection.delete(key)
