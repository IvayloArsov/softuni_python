from project.services.base_service import BaseService


class MainService(BaseService):
    SERVICE = 'MainService'
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, capacity=self.CAPACITY)

    def details(self):
        info_list = [
            f'{self.name} Main Service:',
            f'Robots: {" ".join([robot.name for robot in self.robots]) if self.robots else "none"}'
        ]

        return '\n'.join(info_list)
