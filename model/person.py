from model.entity import Entity


class Person(Entity):

    def __init__(self):
        self.class_name = "person"

    def to_data(self):
        pass