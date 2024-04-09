def get_line(i, n):
    space_count = n - 1 - i
    stars_count = i + 1
    return ' ' * space_count + ('* ' * stars_count).strip()


def get_rhombus(n):
    return [get_line(i, n) for i in range(n)] + \
           [get_line(i, n) for i in range(n - 2, -1, - 1)]


def print_rhombus(n):
    [print(row) for row in get_rhombus(n)]


n = int(input())
print_rhombus(n)
