import os

from redis import StrictRedis

redis = StrictRedis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'], decode_responses=True)
