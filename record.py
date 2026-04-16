class Record:
    def __init__(self, person, location, time):
        self.person = person
        self.location = location
        self.time = time
    def __str__(self):
        return f"Record(person={self.person}, location={self.location}, time={self.time})"
    def get_person(self):
        return self.person
    def get_location(self):
        return self.location
    def get_time(self):
        return self.time
