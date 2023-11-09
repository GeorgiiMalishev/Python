class DoubleElement:
    def __init__(self, *list):
        self.list = list
        self.index = 0

    def __next__(self):
        if self.index >= len(self.list):
            raise StopIteration
        else:
            pair = self.list[self.index:self.index + 2]
            self.index += 2
            if len(pair) == 1:
                pair = (pair[0], None)
            return tuple(pair)

    def __iter__(self):
        return self


dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)
