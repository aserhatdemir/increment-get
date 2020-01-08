from datetime import timedelta

import redis

from Incrementer.incrementer import Incrementer


class RedisIncrementer(Incrementer):

    def __init__(self):
        self.r = None
        self.connect_to_redis()

    def connect_to_redis(self):
        self.r = redis.Redis(host='localhost', port=6379, db=0)
        # self.r.set('global', 0)  --> redis.incr() initialize already

    def get_increment(self, session_id):
        # increment redis value, if the key does not exist initialize the value with 1
        val = self.r.incr(session_id, 1)
        # return {session_id: int(str(self.r.get(session_id), 'utf-8'))}
        return {session_id: val}

    def get_increment_temp(self, session_id):
        # if not self.r.exists(session_id):
        val = self.r.incr(session_id, 1)
        if self.r.ttl(session_id) == -1:
            self.r.expire(session_id, timedelta(seconds=5))
        return {session_id: val}

