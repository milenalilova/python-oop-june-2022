def reverse_text(string):
    index = len(string) - 1
    while index >= 0:
        yield string[index]
        index -= 1


# def reverse_text(text):
#     index = 0
#     n = len(text)
#     while index < n:
#         yield text[n - index - 1]
#         index += 1

for char in reverse_string("step"):
    print(char, end='')