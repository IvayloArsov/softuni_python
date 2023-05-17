tour_days = int(input())

fundraiser = 0
d_wins = 0
d_loses = 0

for day in range(1, tour_days+1):
    daily_fundraiser = 0
    wins = 0
    losses = 0
    while True:

        game = input()

        if game == 'Finish':
            break
        outcome = input()

        if outcome == 'win':
            wins += 1
            daily_fundraiser += 20

        elif outcome == 'lose':
            losses += 1

    if wins > losses:
        d_wins += 1
        daily_fundraiser *= 1.10

    else:
        d_loses += 1

    fundraiser += daily_fundraiser

if d_wins > d_loses:
    fundraiser *= 1.2
    print(f"You won the tournament! Total raised money: {fundraiser:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {fundraiser:.2f}")