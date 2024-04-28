import os

from project.player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        players_names = []
        for p in players:
            if p not in self.players:
                self.players.append(p)
                players_names.append(p.name)
        return f"Successfully added: {', '.join(players_names)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        sustained_player = self.__find_player_by_name(player_name)

        if sustained_player is None:
            return
        if sustenance_type != 'Food' and sustenance_type != 'Drink':
            return

        idx, supply = self.__find_supply_by_type(sustenance_type)

        if supply is None:
            raise Exception(f'There are no {sustenance_type.lower()} supplies left!')

        if not sustained_player.need_sustenance:
            return f'{player_name} have enough stamina.'

        sustained_player.stamina = min(sustained_player.stamina + supply.energy, Player.DEFAULT_STAMINA)
        self.supplies.pop(idx)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        error_message = ''
        if first_player.stamina == 0:
            error_message += f'Player {first_player.name} does not have enough stamina.'

        if second_player.stamina == 0:
            error_message += os.linesep + f'Player {second_player.name} does not have enough stamina.'

        if error_message:
            return error_message.strip()

        if second_player.stamina < first_player.stamina:
            first_player, second_player = second_player, first_player
        first_player_damage = first_player.stamina / 2
        second_player.stamina = max(second_player.stamina - first_player_damage, 0)
        if second_player.stamina == 0:
            return f"Winner: {first_player.name}"

        second_player_damage = second_player.stamina / 2
        first_player.stamina = max(first_player.stamina - second_player_damage, 0)
        if first_player.stamina == 0:
            return f"Winner: {second_player.name}"
        winner = first_player if first_player.stamina > second_player.stamina else second_player

        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        return os.linesep.join([str(p) for p in self.players]) + os.linesep + \
               os.linesep.join([s.details() for s in self.supplies])

    def __find_player_by_name(self, player_name):
        for p in self.players:
            if p.name == player_name:
                return p

    def __find_supply_by_type(self, sustenance_type):
        for idx in range(len(self.supplies) - 1, -1, -1):
            s = self.supplies[idx]
            if s.type == sustenance_type:
                return idx, s
        return -1, None
