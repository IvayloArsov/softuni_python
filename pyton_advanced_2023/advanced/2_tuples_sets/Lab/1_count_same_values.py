input_nums = tuple(float(x) for x in input().split())
uniques = {}
for num in input_nums:
    if num not in uniques:
        uniques[num] = input_nums.count(num)
        print(f"{num} - {input_nums.count(num)} times")
