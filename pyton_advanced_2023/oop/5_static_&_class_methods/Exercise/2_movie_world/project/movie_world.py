from project.dvd import DVD
from project.customer import Customer


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = list()
        self.dvds = list()

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def __get_customer(self, id):
        return [customer for customer in self.customers if id == customer.id][0]

    def __get_dvd(self, id):
        return [x for x in self.dvds if x.id == id][0]

    def rent_dvd(self, customer_id: int, dvd_id: int):
        find_dvd = self.__get_dvd(dvd_id)
        find_customer = self.__get_customer(customer_id)

        if find_dvd in find_customer.rented_dvds:
            return f"{find_customer.name} has already rented {find_dvd.name}"

        if find_dvd.is_rented:
            return "DVD is already rented"

        if find_customer.age < find_dvd.age_restriction:
            return f"{find_customer.name} should be at least {find_dvd.age_restriction} to rent this movie"

        find_customer.rented_dvds.append(find_dvd)
        find_dvd.is_rented = True
        return f"{find_customer.name} has successfully rented {find_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        find_dvd = self.__get_dvd(dvd_id)
        find_customer = self.__get_customer(customer_id)

        if find_dvd in find_customer.rented_dvds:
            find_customer.rented_dvds.remove(find_dvd)
            find_dvd.is_rented = False
            return f"{find_customer.name} has successfully returned {find_dvd.name}"

        return f"{find_customer.name} does not have that DVD"

    def __repr__(self):
        output = ""
        for x in self.customers:
            output += f"{str(x)}\n"
        for x in self.dvds:
            output += f"{str(x)}\n"
        return output.rstrip()


c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world)
