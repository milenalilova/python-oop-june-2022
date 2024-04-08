class Validator:
    @staticmethod
    def validate_if_str_is_empty(string: str, message: str):
        if string == '':
            raise ValueError(message)

    @staticmethod
    def validate_if_price_not_zero_or_less(number: float, message: str):
        if number <= 0:
            raise ValueError(message)
