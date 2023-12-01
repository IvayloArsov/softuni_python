from project.user import User
from project.route import Route
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    cars_dict = {
        'CargoVan': CargoVan,
        'PassengerCar': PassengerCar
    }

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f'{driving_license_number} has already been registered to our platform.'
        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        info_str = (f"{first_name} {last_name} was "
                    f"successfully registered under DLN-{driving_license_number}")
        return info_str

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.cars_dict.keys():
            return f'Vehicle type {vehicle_type} is inaccessible.'
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f'{license_plate_number} belongs to another vehicle.'
        new_vehicle = self.cars_dict[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        info_str = f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."
        return info_str

    def allow_route(self, start_point: str, end_point: str, length: float):
        for existing_route in self.routes:
            if existing_route.start_point == start_point and existing_route.end_point == end_point:
                if existing_route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                if existing_route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."
                if existing_route.length > length:
                    existing_route.is_locked = True
        route_id = len(self.routes) + 1
        new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = next((user for user in self.users if user.driving_license_number == driving_license_number), None)
        if user is not None and user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        vehicle = next((car for car in self.vehicles if car.license_plate_number == license_plate_number), None)
        if vehicle is not None and vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route = next((r for r in self.routes if r.route_id == route_id), None)
        if route is not None and route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()
        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = sorted([
            vehicle
            for vehicle in self.vehicles if vehicle.is_damaged
        ], key=lambda x: (x.brand, x.model))
        count_of_repaired_vehicles = min(count, len(damaged_vehicles))
        for i in range(count_of_repaired_vehicles):
            damaged_vehicles[i].change_status()
            damaged_vehicles[i].recharge()
        info_str = f'{count_of_repaired_vehicles} vehicles were successfully repaired!'
        return info_str

    def users_report(self):
        info_str = ['*** E-Drive-Rent ***']
        users = sorted(self.users, key=lambda x: -x.rating)
        info_str.append('\n'.join(str(user) for user in users))
        return '\n'.join(info_str)

