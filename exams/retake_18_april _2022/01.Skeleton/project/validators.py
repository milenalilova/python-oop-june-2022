def validate_non_empty_string(value, message):
    if not value:
        raise ValueError(message)


def validate_value_above_num(value, num, message):
    if value < num:
        raise ValueError(message)


def validate_value_is_of_type(value, type_obj, message):
    if not isinstance(value, type_obj):
        raise ValueError(message)
