from location import Location


class Crime:
    def __init__(self, victim, time, location=Location, crime_type=str):#should be location=Location but will break things for now, will fix later.
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
