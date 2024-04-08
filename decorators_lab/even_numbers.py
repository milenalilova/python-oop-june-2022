from functools import wraps


def is_even(x):
    return x % 2 == 0


def even_numbers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return [x for x in result if is_even(x)]

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))  # [2, 4]


# def even_numbers(function):
#     def wrapper(numbers):
#         res = [x for x in numbers if x % 2 == 0]
#         return function(res)
#
#     return wrapper
#
# # test code

# @even_numbers
# def get_numbers(numbers):
#     return numbers
#
#
# print(get_numbers([1, 2, 3, 4, 5]))
