class Crime:
    def __init__(self, victim, time, location, crime_type):
        self.victim = victim 
        self.time=time
        self.location=location
        self.crime_type=crime_type
        #could add attributes like weapon, to further complicate later on.
    def get_victim(self):
        return self.victim
    def get_time(self):
        return self.time
    def get_location(self):
        return self.location
    def get_crime_type(self):
        return self.crime_type
