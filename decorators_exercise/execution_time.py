from time import time


def exec_time(func_ref):
    def wrapper(*args):
        # start stopwatch
        start = time()

        # exec func
        func_ref(*args)

        # stop stopwatch
        end = time()

        # return stopped time
        return end - start

    return wrapper


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)]))
