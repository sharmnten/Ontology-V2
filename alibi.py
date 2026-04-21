from event import Event

class Alibi(Event):
    def __init__(self, time, location):
        super().__init__("alibi", {"location": location}, "alibi")
        self.time = time
    def get_time(self):
        return self.time