from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer in self.customers:
            return
        self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer in self.trainers:
            return
        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment in self.equipment:
            return
        self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan in self.plans:
            return
        self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription in self.subscriptions:
            return
        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.__find_by_id(self.subscriptions, subscription_id)
        customer = self.__find_by_id(self.customers, subscription.customer_id)
        trainer = self.__find_by_id(self.trainers, subscription.trainer_id)
        exercise_plan = self.__find_by_id(self.plans, subscription.exercise_id)
        equipment = self.__find_by_id(self.equipment, exercise_plan.equipment_id)

        return repr(subscription) + '\n' + \
               repr(customer) + '\n' + \
               repr(trainer) + '\n' + \
               repr(equipment) + '\n' + \
               repr(exercise_plan)

    def __find_by_id(self, entities, entity_id):
        for entity in entities:
            if entity.id == entity_id:
                return entity


customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))
