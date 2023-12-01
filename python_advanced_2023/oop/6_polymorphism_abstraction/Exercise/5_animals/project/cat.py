from project.animal import Animal


class Cat(Animal):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)

    def __repr__(self):
        info_str = f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}'
        return info_str

    def make_sound(self):
        return 'Meow meow!'
