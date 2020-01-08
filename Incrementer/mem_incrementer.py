from Incrementer.incrementer import Incrementer


class MemIncrementer(Incrementer):

    def __init__(self):
        self.inc_values = {'global': 0}

    def get_global_increment(self):
        return self.increment_and_get('global')

    def increment_and_get(self, session_id):
        if session_id not in self.inc_values.keys():
            self.inc_values[session_id] = 0
        self.inc_values[session_id] += 1
        return {session_id: self.inc_values[session_id]}

    def get_increment(self, session_id):
        return self.increment_and_get(session_id)
