def find_pairs_with_sum(sequence, target):
    num_set = set(sequence)
    found_pairs = set()
    for num in sequence:
        complement = target - num
        if complement in num_set and num != complement:
            pair = (min(num, complement), max(num, complement))
            found_pairs.add(pair)
    return found_pairs


sequence = list(map(int, input().split()))
target = int(input())

pairs = find_pairs_with_sum(sequence, target)
for pair in pairs:
    print(f"{pair[0]} + {pair[1]} = {target}")
