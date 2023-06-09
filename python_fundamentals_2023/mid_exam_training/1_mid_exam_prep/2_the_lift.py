def find_place_on_lift(people, lift_state):
    lift_state = list(map(int, lift_state.split()))
    total_capacity = len(lift_state) * 4

    for i in range(len(lift_state)):
        while lift_state[i] < 4 and people > 0:
            lift_state[i] += 1
            people -= 1
            if lift_state[i] == 4 or people == 0:
                break

    if people == 0 and sum(lift_state) < total_capacity:
        print("The lift has empty spots!")
        print(" ".join(map(str, lift_state)))
    elif people > 0 and sum(lift_state) == total_capacity:
        print(f"There isn't enough space! {people} people in a queue!")
        print(" ".join(map(str, lift_state)))
    else:
        print(" ".join(map(str, lift_state)))


people_waiting = int(input())
lift = input()

find_place_on_lift(people_waiting, lift)
