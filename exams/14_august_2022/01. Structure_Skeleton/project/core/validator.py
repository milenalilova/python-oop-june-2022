class Validator:
    @staticmethod
    def validate_non_empty_string_or_white_spaces(value, message):
        if not value.strip():
            raise ValueError(message)

    @staticmethod
    def validate_value_above_minimum(value, min_num, message):
        if value < min_num:
            raise ValueError(message)

    @staticmethod
    def validate_length_above_minimum(value, min_num, message):
        if len(value) < min_num:
            raise ValueError(message)

    @staticmethod
    def validate_value_does_not_exceed_limit(value, max_num, message):
        if value > max_num:
            raise ValueError(message)

    @staticmethod
    def validate_type_is_valid(value, values_list, message):
        if value not in values_list:
            raise ValueError(message)
