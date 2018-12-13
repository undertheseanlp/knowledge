class Entity:
    def __init__(self):
        self.name = ""
        self.class_name = ""

    def to_data(self):
        raise NotImplementedError
