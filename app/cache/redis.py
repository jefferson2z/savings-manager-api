from redis import Redis

from app.config import settings

redis_address = settings.get_redis_address()

redisConnection = Redis.from_url(redis_address)
