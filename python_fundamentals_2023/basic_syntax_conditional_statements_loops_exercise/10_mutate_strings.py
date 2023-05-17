def mutate(s1, s2):
    if s1 == s2:
        return s1
    else:
        for index in range(len(s1)):
            if s1[index] != s2[index]:
                s1 = s2[:index + 1] + s1[index + 1:]
                print(s1)


str_1 = input()
str_2 = input()
mutate(str_1, str_2)