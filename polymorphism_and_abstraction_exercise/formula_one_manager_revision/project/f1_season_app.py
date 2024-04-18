from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    def __init__(self, red_bull_team: RedBullTeam = None, mercedes_team: MercedesTeam = None):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int):
        valid_team_names = ['Red Bull', 'Mercedes']
        if team_name not in valid_team_names:
            raise ValueError('Invalid team name!')
        if team_name == 'Red Bull':
            self.red_bull_team = RedBullTeam(budget)
        elif team_name == 'Mercedes':
            self.mercedes_team = MercedesTeam(budget)
        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if self.red_bull_team is None or self.mercedes_team is None:
            raise Exception('Not all teams have registered for the season.')

        better_position_team = ''
        if red_bull_pos < mercedes_pos:
            better_position_team = 'Red Bull'
        else:
            better_position_team = 'Mercedes'

        red_bull_result = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes_result = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)
        return f"Red Bull: {red_bull_result}. Mercedes: {mercedes_result}. {better_position_team} is ahead at the {race_name} race."
