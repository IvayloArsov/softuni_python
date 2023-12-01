class vowels:
    def __init__(self, input_str):
        self.input_str = input_str
        self.vowels = 'AaEeOoIiUuYy'
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_index < len(self.input_str):
            cur_val = self.input_str[self.current_index]
            self.current_index += 1
            if cur_val in self.vowels:
                return cur_val

        raise StopIteration


# my_string = vowels('ASDFA[SOIFDSDFSAODI[MNFA[SOINFFO[ISANFSAOIFNASOIF]EW[IONCISFSODINFO')
# for char in my_string:
#     print(char)
