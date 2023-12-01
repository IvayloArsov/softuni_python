from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    WEIGHT = 7
    TYPE_ = 'FemaleRobot'
    SERVICE = 'SecondaryService'
    INCREMENT_STEP = 1

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=self.WEIGHT)

    def eating(self):
        self.weight += self.INCREMENT_STEP
