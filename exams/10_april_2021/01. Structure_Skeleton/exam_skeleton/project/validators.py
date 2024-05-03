def validate_non_empty_string(value, message):
    if not value:
        raise ValueError(message)


def validate_value_not_negative_or_zero(value, message):
    if value <= 0:
        raise ValueError(message)
