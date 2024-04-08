class Validator:
    @staticmethod
    def raise_if_str_is_empty(string: str, message: str):
        if string == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_less_than_or_equal_to_zero(number: float, message: str):
        if number <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_len_is_less_than(obj, min_len, message):
        if len(obj) < min_len:
            raise ValueError(message)

    @staticmethod
    def raise_if_num_is_not_in_range(number, min_number, max_number, message):
        if number < min_number or number > max_number:
            raise ValueError(message)

    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string: str, message: str):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_zero_or_negative(number: float, message):
        if number <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_not_in_range(number: int, min_value: int, max_value: int, message: str):
        if number < min_value or number > max_value:
            raise ValueError(message)

    def __find_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def __find_supply_by_type(self, sustenance_type):
        for idx in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[idx]
            if supply.__class__.__name__ == sustenance_type:
                return (idx, supply)
        return (-1, None)