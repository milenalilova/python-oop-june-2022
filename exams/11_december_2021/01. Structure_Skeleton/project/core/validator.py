class Validator:
    @staticmethod
    def validate_value_has_min_length(value, min_length, message):
        if len(value) < min_length:
            raise ValueError(message)

    @staticmethod
    def validate_value_in_range(value, min_value, max_value, message):
        if not min_value <= value <= max_value:
            raise ValueError(message)
