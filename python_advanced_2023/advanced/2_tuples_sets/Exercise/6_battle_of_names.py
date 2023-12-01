input_lines = int(input())
row = 0
odd_sets = set()
even_sets = set()

for _ in range(input_lines):
    name_ascii_sum = list(input())
    row += 1
    current_sum = sum(ord(char) for char in name_ascii_sum)
    current_sum //= row
    if current_sum % 2 == 0:
        even_sets.add(current_sum)
    else:
        odd_sets.add(current_sum)

odds = sum(odd_sets)
evens = sum(even_sets)

if odds == evens:
    result = odd_sets.union(even_sets)
elif odds > evens:
    result = odd_sets.difference(even_sets)
elif odds < evens:
    result = odd_sets.symmetric_difference(even_sets)

print(", ".join(map(str, result)))