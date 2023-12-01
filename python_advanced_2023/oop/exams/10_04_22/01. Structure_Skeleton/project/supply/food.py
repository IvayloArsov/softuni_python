from project.supply.supply import Supply


class Food(Supply):
    type_ = 'Food'
    def __init__(self, name):
        super().__init__(name, energy=25)

