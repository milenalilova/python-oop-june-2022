def vowel_filter(function):
    def wrapper():
        result = function()
        vowels_list = [ch for ch in result if ch.lower() in 'aouei']
        return vowels_list
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
