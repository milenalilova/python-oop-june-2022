def store_results(func_ref):
    def wrapper(*args):
        result = func_ref(*args)
        with open("./results.txt", "a") as file:
            file.write(f"Function '{func_ref.__name__}' was add called. Result: {result}")
            file.write("\n")
        return result

    return wrapper


@store_results
def mult(a, b):
    return a * b


@store_results
def add(a, b):
    return a + b


print(add(2, 2))
print(mult(6, 4))
