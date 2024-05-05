class Validator:

    @staticmethod
    def validate_non_empty_string_or_white_space(value, message):
        if not value or value == ' ':
            raise ValueError(message)

    @staticmethod
    def validate_value_not_negative_or_zero(value, message):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def validate_value_in_range(value, min_value, max_value, message):
        if not min_value <= value <= max_value:
            raise ValueError(message)
