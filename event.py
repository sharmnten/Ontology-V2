class Event:
    def __init__(self, name, data=None, type=str):
        self.name = name
        self.data = data
        self.type = type
    def __str__(self):
        return f"Event(name={self.name}, data={self.data}, type={self.type})"
    def get_name(self):
        return self.name
    def get_data(self):
        return self.data
    def get_type(self):
        return self.type