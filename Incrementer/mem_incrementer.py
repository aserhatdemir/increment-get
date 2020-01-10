from Incrementer.incrementer import Incrementer


class MemIncrementer(Incrementer):

    def __init__(self):
        self.inc_values = {'global': 0}

    def get_increment(self, session_id):
        if session_id not in self.inc_values.keys():
            self.inc_values[session_id] = 0
        self.inc_values[session_id] += 1
        return self.get_value(session_id)

    def get_value(self, session_id):
        return {session_id: self.inc_values[session_id]}

    def set_value(self, session_id, val):
        self.inc_values[session_id] = val
        if self.get_value(session_id):
            return self.get_value(session_id)
        return None





