from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)

    @property
    def team_expenses(self):
        expenses = 250000
        return expenses

    def calculate_revenue_after_race(self, race_pos: int):
        earned_from_sponsors = 0
        # Sponsor 'Oracle'
        if race_pos == 1:
            earned_from_sponsors += 1500000
        elif race_pos == 2:
            earned_from_sponsors += 800000
        # Sponsor 'Honda'
        if race_pos <= 8:
            earned_from_sponsors += 20000
        elif race_pos <= 10:
            earned_from_sponsors += 10000
        revenue = earned_from_sponsors - self.team_expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
