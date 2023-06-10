player_name = input() # 1st player name input

highest_score = 0  # placeholder for highest score
winner = ''  # placeholder for the player with the highest score
# both of these need to be outside the loop so they don't get overwritten

while player_name != 'Stop':

    score = 0

    for i in range(len(player_name)):  # number of guesses based on the length of the player's name
        guess = int(input())

        if guess != ord(player_name[i]):
            # checks if the player's guess is equal to the ascii of the player's name
            # i is the step in the cycle, and corresponds to the name's letter, so e.g. 3rd step is player[3]
            score += 2
        else:
            score += 10

        if score >= highest_score:  # if the summed score is more than the highest score, replace it.
            highest_score = score
            winner = player_name

    player_name = input()  # repeats the cycle if command "Stop" is not given.

    if player_name == 'Stop':
        print(f'The winner is {winner} with {highest_score} points!')
        break