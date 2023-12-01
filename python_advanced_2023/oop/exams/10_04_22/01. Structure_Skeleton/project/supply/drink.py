from project.supply.supply import Supply


class Drink(Supply):
    type_ = 'Drink'
    def __init__(self, name):
        super().__init__(name, energy=15)
