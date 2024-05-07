class Validator:
    @staticmethod
    def validate_non_empty_string_or_white_spaces(value, message):
        if not value.strip():
            raise ValueError(message)

    @staticmethod
    def validate_value_not_negative_or_zero(value, message):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def validate_value_not_negativ(value, message):
        if value < 0:
            raise ValueError(message)

    @staticmethod
    def validate_value_is_unique(value, values_set, message):
        if value in values_set:
            raise Exception(message)
