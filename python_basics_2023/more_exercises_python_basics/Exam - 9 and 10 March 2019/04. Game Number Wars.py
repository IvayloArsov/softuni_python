name_1 = input()
name_2 = input()

player1_score = 0
player2_score = 0

player1_card = input()

while player1_card != 'End of game':
    player1_card = int(player1_card)
    player2_card = int(input())

    difference__ = abs(player2_card-player1_card)

    if player1_card > player2_card:
        player1_score += difference__
    elif player1_card < player2_card:
        player2_score += difference__
    else:
        player1_card = int(input())
        player2_card = int(input())

        if player1_card > player2_card:
            winner = name_1
            win_points = player1_score+difference__
        elif player1_card < player2_card:
            winner = name_2
            win_points = player2_score + difference__

        print('Number wars!')
        print(f'{winner} is winner with {win_points} points')
        break
    player1_card = input()
else:
    print(f"{name_1} has {player1_score} points")
    print(f"{name_2} has {player2_score} points")