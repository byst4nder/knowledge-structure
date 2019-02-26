# encoding=utf-8
import redis


class RedisHelper:
    def __init__(self, host='192.168.85.20', port=6379):
        self.__redis = redis.Redis(host, port)

    def get(self, key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return None

    def set(self, key, value):
        self.__redis.set(key, value)


