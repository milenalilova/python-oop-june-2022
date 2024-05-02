from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for r in self.rooms:
            total_consumption += r.room_cost + r.expenses
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []
        for r in self.rooms:
            output = ''
            bill = r.room_cost + r.expenses
            if bill <= r.budget:
                r.budget -= bill
                output = f"{r.family_name} paid {bill:.2f}$ and have {r.budget:.2f}$ left."
            else:
                self.rooms.remove(r)
                output = f"{r.family_name} does not have enough budget and must leave the hotel."
            result.append(output)
        return '\n'.join(result)

    def status(self):
        all_people_in_the_hotel = sum([r.members_count for r in self.rooms])

        output = ''

        output += f"Total population: {all_people_in_the_hotel}" + '\n'
        for r in self.rooms:
            output += f"{r.family_name} with {r.members_count} members. Budget: {r.budget:.2f}$, Expenses: {r.expenses:.2f}$" + '\n'

            if r.children:
                for idx, c in enumerate(r.children):
                    output += f"--- Child {idx + 1} monthly cost: {c.get_monthly_expense():.2f}$" + '\n'

            if r.appliances:
                cost_of_all_appliances_for_one_month = sum([a.get_monthly_expense() for a in r.appliances])
                output += f"--- Appliances monthly cost: {cost_of_all_appliances_for_one_month:.2f}$" + '\n'

        return output.strip()

