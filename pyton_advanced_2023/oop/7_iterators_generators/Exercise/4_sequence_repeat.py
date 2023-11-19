class sequence_repeat:
    def __init__(self, sequence, number: int):
        self.string = sequence
        self.length = number
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= self.length:
            raise StopIteration

        current_char = self.string[self.current_index % len(self.string)]
        self.current_index += 1

        return current_char


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

