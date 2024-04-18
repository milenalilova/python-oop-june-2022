from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)

    # @property
    # def team_sponsors(self):
    #     sponsors_dict = {
    #         1: [1000000],
    #         3: [500000],
    #         5: [100000],
    #         7: [50000]
    #     }
    #     return sponsors_dict

    @property
    def team_expenses(self):
        expenses = 200000
        return expenses

    def calculate_revenue_after_race(self, race_pos: int):
        earned_from_sponsors = 0
        # Sponsor 'Petronas'
        if race_pos == 1:
            earned_from_sponsors += 1000000
        elif race_pos == 3:
            earned_from_sponsors += 500000
        # Sponsor 'TeamViewer'
        if race_pos <= 5:
            earned_from_sponsors += 100000
        elif race_pos <= 7:
            earned_from_sponsors += 50000
        revenue = earned_from_sponsors - self.team_expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
