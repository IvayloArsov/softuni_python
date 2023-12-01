from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    services_dict = {
        'MainService': MainService,
        'SecondaryService': SecondaryService
    }
    robots_dict = {
        'MaleRobot': MaleRobot,
        'FemaleRobot': FemaleRobot
    }

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.services_dict:
            raise Exception("Invalid service type!")
        new_service = self.services_dict[service_type](name)
        self.services.append(new_service)
        info_str = f'{service_type} is successfully added.'
        return info_str

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.robots_dict:
            raise Exception("Invalid robot type!")
        new_robot = self.robots_dict[robot_type](name, kind, price)
        self.robots.append(new_robot)
        info_str = f"{robot_type} is successfully added."
        return info_str

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.find_robot_by_name(robot_name)
        service = self.find_service_by_name(service_name)
        if robot.SERVICE != service.SERVICE:
            return "Unsuitable service."
        if service.CAPACITY <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")
        self.robots.remove(robot)
        service.robots.append(robot)
        info_str = f"Successfully added {robot_name} to {service_name}."
        return info_str

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.find_service_by_name(service_name)
        robot = [robot for robot in service.robots if robot.name == robot_name]
        if not robot:
            raise Exception("No such robot in this service!")
        robot = robot[0]
        service.robots.remove(robot)
        self.robots.append(robot)
        info_str = f"Successfully removed {robot_name} from {service_name}."
        return info_str

    def feed_all_robots_from_service(self, service_name: str):
        service = self.find_service_by_name(service_name)
        for robot in service.robots:
            robot.eating()
        info_str = f"Robots fed: {len(service.robots)}."
        return info_str

    def service_price(self, service_name: str):
        service = self.find_service_by_name(service_name)
        total_service_price = sum([robot.price for robot in service.robots])
        info_str = f"The value of service {service_name} is {total_service_price:.2f}."
        return info_str

    def __str__(self):
        return '\n'.join([service.details() for service in self.services])

    # made myself some helper functions for more readability lmao
    def find_service_by_name(self, service_name):
        service = [s for s in self.services if s.name == service_name]
        return service[0]

    def find_robot_by_name(self, robot_name):
        robot = [r for r in self.robots if r.name == robot_name]
        return robot[0]
