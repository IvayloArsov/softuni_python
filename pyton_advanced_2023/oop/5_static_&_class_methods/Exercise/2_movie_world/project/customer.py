class Customer:
    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = list()

    def __repr__(self):
        info_str = f'{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD\'s ({", ".join(f.name for f in self.rented_dvds)})'
        return info_str
