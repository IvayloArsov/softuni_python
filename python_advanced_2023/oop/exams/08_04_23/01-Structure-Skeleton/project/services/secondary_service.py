from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15
    SERVICE = 'SecondaryService'

    def __init__(self, name: str):
        super().__init__(name, capacity=self.CAPACITY)

    def details(self):
        info_list = [
            f'{self.name} Secondary Service:',
            f'Robots: {" ".join([robot.name for robot in self.robots]) if self.robots else "none"}'
        ]

        return '\n'.join(info_list)
