class Integer:
    def __init__(self, value: int):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = None

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            new_instance = cls(int(float_value))
            return new_instance
        return 'value is not a float'

    @classmethod
    def from_string(cls, string_value):
        if isinstance(string_value, str):
            try:
                integer_value = int(string_value)
                new_instance = cls(integer_value)
                return new_instance
            except ValueError:
                return "wrong type"
        else:
            return 'wrong type'

    @classmethod
    def from_roman(cls, roman_value):
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        def roman_to_int(s):
            result = 0
            prev_value = 0
            for numeral in s[::-1]:
                if roman_numerals[numeral] < prev_value:
                    result -= roman_numerals[numeral]
                else:
                    result += roman_numerals[numeral]
                prev_value = roman_numerals[numeral]
            return result

        if isinstance(roman_value, str) and all(char in roman_numerals for char in roman_value):
            integer_value = roman_to_int(roman_value)
            new_instance = cls(integer_value)
            return new_instance
        return 'wrong type'

#
# first_num = Integer(10)
# print(first_num.value)
#
# second_num = Integer.from_roman("IV")
# print(second_num.value)
#
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))
