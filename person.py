from event import Event
from alibi import Alibi

class Person:
    def __init__(self, name, events=None):
        self.name = name
  
        self.events = events or {}
        self.status = "alive"
    def get_name(self):
        return self.name
    def get_location(self, time):
        current_location = None

        for t in sorted(self.events):
            if t > time:
                break

            event = self.events[t]

            if event.name == "enter":
                current_location = event.data.get("location")
            elif event.name == "leave":
                current_location = None

        return current_location

    def make_alibi(self, time, location=[]):
        alibi_log = []
        for t in time:
            alibi_log.append(Alibi(t, location))
        return alibi_log
