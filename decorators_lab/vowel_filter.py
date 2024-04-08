from functools import wraps


def vowel_filter(func):
    vowels = 'eyuioa'

    @wraps(func)
    def wrapper():
        result = func()
        return [x for x in result if x.lower() in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ['a', 'b', 'c', 'd', 'e']


@vowel_filter
def get_name():
    return 'Doncho Minkov'


print(get_letters())  # ['a', 'e']
print(get_name())




# def vowel_filter(function):
#     def wrapper():
#         res = function()
#         filtered = [x for x in res if x.lower() in "aeiou"]
#         return filtered
#
#     return wrapper
#
#
# # test code
#
# @vowel_filter
# def get_letters():
#     return ["a", "b", "c", "d", "e"]
#
#
# print(get_letters())
