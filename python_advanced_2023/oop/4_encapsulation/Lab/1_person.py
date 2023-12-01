class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_age(self):
        self.age = self.__age
        return self.age

    def get_name(self):
        self.name = self.__name
        return self.name



