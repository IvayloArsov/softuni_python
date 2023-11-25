from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    WEIGHT = 9
    TYPE_ = 'MaleRobot'
    SERVICE = 'MainService'
    INCREMENT_STEP = 3

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=self.WEIGHT)

    def eating(self):
        self.weight += self.INCREMENT_STEP
