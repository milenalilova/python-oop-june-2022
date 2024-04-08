class Validator:
    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string: str, message: str):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def validate_if_number_less_then_eighteen(number: int, message: str):
        if number < 18:
            raise ValueError(message)

    @staticmethod
    def raise_if_len_is_less_than(string, min_len, message):
        if len(string) < min_len:
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_bigger_than_max_number(number, max_number, message):
        if number > max_number:
            raise ValueError(message)
