n = int(input())
positives = []
negatives = []
for _ in range(n):
    num = int(input())
    if num < 0:
        negatives.append(num)
    elif num > 0:
        positives.append(num)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")