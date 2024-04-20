class dictionary_iter:
    def __init__(self, dictionary):
        self.items = list(dictionary.items())
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == len(self.items):
            raise StopIteration
        result = self.items[self.idx]
        self.idx += 1
        return result


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result2 = dictionary_iter({"name": "Peter", "age": 24})
for x in result2:
    print(x)
