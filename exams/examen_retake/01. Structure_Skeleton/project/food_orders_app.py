from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    RECEIPT_ID = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception('The client has already been registered!')
        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if not isinstance(meal, Meal):
                continue
            self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        result = ''
        for meal in self.menu:
            result += meal.details() + '\n'
        return result.strip()

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        # find client by phone number first
        client = self.__find_client_by_phone_number(client_phone_number)
        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        for meal in meal_names_and_quantities:
            if meal not in self.menu:
                if client.shopping_cart:
                    client.shopping_cart.clear()
                    client.bill = 0
                raise Exception(f'{meal} is not on the menu!')
            if meal_names_and_quantities[meal] > len(self.menu):
                raise Exception(f"Not enough quantity of {meal}: {meal_names_and_quantities[meal]}!")

            client.shopping_cart.append(meal)
            client.bill += meal.price

    def cancel_order(self, client_phone_number: str):
        client = self.__find_client_by_phone_number(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        client.shopping_cart.clear()
        client.bill = 0
        raise f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__find_client_by_phone_number(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        self.RECEIPT_ID += 1
        total_paid_money = client.bill
        client.bill = 0
        client.shopping_cart.clear()
        return f"Receipt #{self.RECEIPT_ID} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def __find_client_by_phone_number(self, phone_number):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client
