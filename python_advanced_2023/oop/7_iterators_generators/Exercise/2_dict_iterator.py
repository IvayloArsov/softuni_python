class dictionary_iter:
    def __init__(self, dict_obj: dict):
        self.dict_obj = dict_obj
        self.keys = list(dict_obj.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.keys):
            key = self.keys[self.index]
            value = self.dict_obj[key]
            result = (key, value)
            self.index += 1
            return result
        raise StopIteration


# result = dictionary_iter({"name": "Peter", "age": 24})
# for x in result:
#     print(x)
#
# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)
