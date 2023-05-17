tourney_name = input()
win = 0
loss = 0

while tourney_name != 'End of tournaments':
    num_games = int(input())
    for i in range(1, num_games+1):
        home_t = int(input())
        away_t = int(input())

        diff = abs(home_t-away_t)

        if home_t > away_t:
            win += 1
            result = 'win'
        elif home_t < away_t:
            loss += 1
            result = 'lost'

        print(f'Game {i} of tournament {tourney_name}: {result} with {diff} points.')

    tourney_name = input()


print(f"{(win / (win + loss)) * 100:.2f}% matches win")
print(f"{(loss / (win + loss)) * 100:.2f}% matches lost")