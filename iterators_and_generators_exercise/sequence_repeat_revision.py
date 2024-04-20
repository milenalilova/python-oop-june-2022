class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.number:
            raise StopIteration
        result = self.sequence[self.idx % len(self.sequence)]
        self.idx += 1
        return result


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

print()

result1 = sequence_repeat('I Love Python', 3)
for item in result1:
    print(item, end='')
