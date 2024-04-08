def genrange(start, end):
    i = start
    n = end

    while i <= n:
        yield i
        i += 1


print(list(genrange(1, 10)))
print(sum(genrange(1, 10)))
