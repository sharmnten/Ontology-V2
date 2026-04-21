class Location: 
    def __init__(self, name=str, size=int):
        self.name = name
        self.size = size
    def get_name(self):
        return self.name
    def get_size(self):
        return self.size