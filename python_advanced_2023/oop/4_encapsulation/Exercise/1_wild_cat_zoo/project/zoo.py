from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
# from project.animal import Animal
# from project.worker import Worker

class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = list()
        self.workers = list()

    def get_budget(self):
        return self.__budget

    def profit(self, new_budget):
        self.__budget += new_budget

    def get_animal_capacity(self):
        return self.__animal_capacity

    def set_animal_capacity(self, quantity):
        self.__animal_capacity += quantity

    def get_workers_capacity(self):
        return self.__workers_capacity

    def set_workers_capacity(self, quantity):
        self.__workers_capacity += quantity

    def add_animal(self, animal, price):
        if self.get_animal_capacity() > 0:
            if self.get_budget() >= price:
                self.profit(-price)
                self.set_animal_capacity(-1)
                self.animals.append(animal)
                return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
            return 'Not enough budget'
        return 'Not enough space for animal'

    def hire_worker(self, worker):
        if self.get_workers_capacity() > len(self.workers):
            self.workers.append(worker)
            # self.set_workers_capacity(-1)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        return 'Not enough space for worker'

    def fire_worker(self, worker_name):
        if not self.workers:
            return f'There is no {worker_name} in the zoo'
        for index, worker in enumerate(self.workers):
            if worker.name == worker_name:
                del self.workers[index]
                # self.set_workers_capacity(1)
                return f'{worker.name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        workers_upkeep = 0
        for worker in self.workers:
            workers_upkeep += worker.salary
        if self.get_budget() >= workers_upkeep:
            self.profit(-workers_upkeep)
            return f'You payed your workers. They are happy. Budget left: {self.get_budget()}'
        return f'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        animal_upkeep = 0
        for animal in self.animals:
            animal_upkeep += animal.money_for_care
        if self.get_budget() >= animal_upkeep:
            self.profit(-animal_upkeep)
            return f'You tended all the animals. They are happy. Budget left: {self.get_budget()}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def animals_status(self):
        lions = [animal for animal in self.animals if isinstance(animal, Lion)]
        tigers = [animal for animal in self.animals if isinstance(animal, Tiger)]
        cheetahs = [animal for animal in self.animals if isinstance(animal, Cheetah)]

        animals_status_string = f"You have {len(self.animals)} animals\n"
        animals_status_string += f"----- {len(lions)} Lions:\n"
        animals_status_string += "\n".join([f"{lion}" for lion in lions]) + "\n"
        animals_status_string += f"----- {len(tigers)} Tigers:\n"
        animals_status_string += "\n".join([f"{tiger}" for tiger in tigers]) + "\n"
        animals_status_string += f"----- {len(cheetahs)} Cheetahs:\n"
        animals_status_string += "\n".join([f"{cheetah}" for cheetah in cheetahs])
        return animals_status_string

    def workers_status(self):
        keepers = [worker for worker in self.workers if isinstance(worker, Keeper)]
        caretakers = [worker for worker in self.workers if isinstance(worker, Caretaker)]
        vets = [worker for worker in self.workers if isinstance(worker, Vet)]

        workers_status_string = f"You have {len(self.workers)} workers\n"
        workers_status_string += f"----- {len(keepers)} Keepers:\n"
        workers_status_string += "\n".join([f"{keeper}" for keeper in keepers]) + "\n"
        workers_status_string += f"----- {len(caretakers)} Caretakers:\n"
        workers_status_string += "\n".join([f"{caretaker}" for caretaker in caretakers]) + "\n"
        workers_status_string += f"----- {len(vets)} Vets:\n"
        workers_status_string += "\n".join([f"{vet}" for vet in vets])
        return workers_status_string


