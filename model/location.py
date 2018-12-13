class Location:
    def __init__(self, name=None, level=None):
        self.name = name
        self.level = level

    def set_name(self, name):
        self.name = name

    def set_level(self, level):
        self.level = level

    def to_data(self):
        data = {}
        data["name"] = self.name
        data["level"] = self.level
        return data