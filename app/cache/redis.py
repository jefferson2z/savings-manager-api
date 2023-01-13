from redis import Redis

from app.config import settings

redis_address = settings.get_redis_address()

redisConnection = Redis(host=redis_address["host"], port=redis_address["port"], db=0)
