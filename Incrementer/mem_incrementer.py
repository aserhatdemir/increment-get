from Incrementer.incrementer import Incrementer


class MemIncrementer(Incrementer):

    def __init__(self):
        self.inc_values = {'global': 0}

    def get_global_increment(self):
        return self.increment_and_get('global')

    def get_increment(self, session_id):
        return self.increment_and_get(session_id)

    def increment_and_get(self, session_id):
        if session_id not in self.inc_values.keys():
            self.inc_values[session_id] = 0
        self.inc_values[session_id] += 1
        return {session_id: self.inc_values[session_id]}

    # make the commit and push work comment

    # def get_increment(self, session_id):
    #     # increment redis value, if the key does not exist initialize the value with 1
    #     val = self.r.incr(session_id, 1)
    #     # return {session_id: int(str(self.r.get(session_id), 'utf-8'))}
    #     return {session_id: val}
    #
    # def get_increment_temp(self, session_id):
    #     # if not self.r.exists(session_id):
    #     val = self.r.incr(session_id, 1)
    #     if self.r.ttl(session_id) == -1:
    #         self.r.expire(session_id, timedelta(seconds=5))
    #     return {session_id: val}
    #
    # def get_value(self, session_id):
    #     return {session_id: int(str(self.r.get(session_id), 'utf-8'))}
    #
    # def set_value(self, session_id, val):
    #     if self.r.mset({session_id: val}):
    #         return self.get_value(session_id)
    #     return None
    #
