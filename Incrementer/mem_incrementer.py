from Incrementer.incrementer import Incrementer

import threading
import time


class MemIncrementer(Incrementer):

    def __init__(self):
        self.inc_values = {'global': 0}
        self.lock = threading.Lock()

    def get_increment(self, session_id):
        self.lock.acquire()
        if session_id not in self.inc_values.keys():
            self.inc_values[session_id] = 0
        self.inc_values[session_id] += 1
        ret = self.get_value(session_id)
        self.lock.release()
        return ret

    def get_value(self, session_id):
        if session_id not in self.inc_values.keys():
            return None
        ret = {session_id: self.inc_values[session_id]}
        return ret

    def set_value(self, session_id, val):
        self.lock.acquire()
        self.inc_values[session_id] = val
        ret = self.get_value(session_id)
        self.lock.release()
        if ret:
            return ret
        return None





