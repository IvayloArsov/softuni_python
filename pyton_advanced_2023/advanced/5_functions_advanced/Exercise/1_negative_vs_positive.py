def pos_vs_negs(numbers):
    positives = [num for num in numbers if num > 0]
    negatives = [num for num in numbers if num < 0]
    print(sum(negatives))
    print(sum(positives))
    if abs(sum(negatives)) > sum(positives):
        return "The negatives are stronger than the positives"
    else:
        return "The positives are stronger than the negatives"


arr_nums = list(map(int, input().split()))
print(pos_vs_negs(arr_nums))
