def memory_game():
    sequence = input().split()
    turns = 0

    while True:
        command = input()

        if command == 'end':
            break

        first_position, second_position = map(int, command.split())
        guess = [first_position, second_position]
        if first_position == second_position or any(x >= len(sequence) or x < 0 for x in guess):
            turns += 1
            el = f"-{turns}a"
            sequence.insert(len(sequence)//2, el)
            sequence.insert(len(sequence)//2, el)
            print('Invalid input! Adding additional elements to the board')

        elif sequence[first_position] == sequence[second_position]:
            found_element1, found_element2 = sequence[first_position], sequence[second_position]
            turns += 1
            print(f"Congrats! You have found matching elements - {found_element1}!")
            sequence.remove(found_element1)
            sequence.remove(found_element2)
        else:
            turns += 1
            print("Try again!")

        if len(sequence) == 0:
            print(f'You have won in {turns} turns!')
            return
    print("Sorry you lose :(")
    print(" ".join(map(str, sequence)))


memory_game()