best_player = ''
high_score = 0

while True:
    name = input()
    if name == 'END':
        break

    goals = int(input())

    if goals >= 10:
        high_score = goals
        best_player = name
        break

    if goals > high_score:
        high_score = goals
        best_player = name


print(f'{best_player} is the best player!')

if high_score >= 3:
    print(f"He has scored {high_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {high_score} goals.")
