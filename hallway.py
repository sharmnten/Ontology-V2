
from location import Location



class Hallway:
    def __init__(self,name=str, location1=Location, location2=Location):
        self.name = name
        self.location1 = location1
        self.location2 = location2
    def get_connections(self):
        return (self.location1, self.location2)