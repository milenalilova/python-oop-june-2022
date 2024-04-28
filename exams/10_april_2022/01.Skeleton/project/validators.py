def validate_non_empty_string(value, message):
    if not value:
        raise ValueError(message)


def validate_value_is_unique(value, set, message):
    if value in set:
        raise Exception(message)


def validate_value_not_negative(value, message):
    if value < 0:
        raise ValueError(message)


def validate_value_above_num(value, num, message):
    if value < num:
        raise ValueError(message)


def validate_value_in_range(value, min_value, max_value, message):
    if not min_value <= value <= max_value:
        raise ValueError(message)
