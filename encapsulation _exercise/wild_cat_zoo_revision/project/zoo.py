from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary
        if self.__budget < total_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_money_for_care = 0
        for animal in self.animals:
            total_money_for_care += animal.money_for_care
        if self.__budget < total_money_for_care:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [repr(a) for a in self.animals if isinstance(a, Lion)]
        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]

        output = f"You have {len(self.animals)} animals\n"
        output += f"----- {len(lions)} Lions:\n" + '\n'.join(lions) + '\n'
        output += f"----- {len(tigers)} Tigers:\n" + '\n'.join(tigers) + '\n'
        output += f"----- {len(cheetahs)} Cheetahs:\n" + '\n'.join(cheetahs) + '\n'
        return output.strip()

    def workers_status(self):
        keepers = [repr(w) for w in self.workers if isinstance(w, Keeper)]
        caretakers = [repr(w) for w in self.workers if isinstance(w, Caretaker)]
        vets = [repr(w) for w in self.workers if isinstance(w, Vet)]

        output = f"You have {len(self.workers)} workers\n"
        output += f"----- {len(keepers)} Keepers:\n" + '\n'.join(keepers) + '\n'
        output += f"----- {len(caretakers)} Caretakers:\n" + '\n'.join(caretakers) + '\n'
        output += f"----- {len(vets)} Vets:\n" + '\n'.join(vets) + '\n'
        return output.strip()
