seq_numbers = [int(num) for num in input().split(", ")]


threshold = 10
while len(seq_numbers) > 0:
    filtered = list(filter(lambda x: threshold-10 < x <= threshold, seq_numbers))
    for item in filtered:
        seq_numbers.remove(item)
    print(f"Group of {threshold}'s: {filtered}")
    threshold += 10
