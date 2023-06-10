n = int(input())
counter = 0
numbers = []
for i in range(0, n*2):
    num = int(input())
    numbers.append(num)
    
sums = []

for i in range(0, 2*n, 2):
    pair_sum = numbers[i]+numbers[i+1]
    sums.append(pair_sum)

diffs = []

for i in range(len(sums)-1):
    diff = abs(sums[i+1]-sums[i])
    diffs.append(diff)

if n == 1:
    max_diff = max(sums)
    print(f"Yes, value={max(sums)}")

else:
    max_diff = max(diffs)
    if max_diff == 0:
        print(f"Yes, value={max(sums)}")
    else:
        print(f'No, maxdiff={max_diff}')