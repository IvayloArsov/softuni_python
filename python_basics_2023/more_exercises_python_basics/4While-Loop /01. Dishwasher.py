bottles = int(input())
detergent = bottles * 750
counter = 0
dishes = 0
pots = 0
total_wasted = 0
while True:
    washed = input()
    if detergent >0:
        washed = int(input())
        detergent -= (washed *5)
        total_wasted += (washed * 5)
        counter += 1
        dishes += washed
        if counter == 3:
            counter = 0
            detergent -= washed * 15
            total_wasted += washed * 15
            pots += washed
        if detergent < 0:
            print(f'Not enough detergent, {total_wasted - detergent} ml. more necessary!')
            break
    elif washed == 'End':
        print("Detergent was enough!")
        print(f"{dishes} dishes and {pots} pots were washed.")
        print(f'Leftover detergent {detergent - total_wasted} ml.')
        break
