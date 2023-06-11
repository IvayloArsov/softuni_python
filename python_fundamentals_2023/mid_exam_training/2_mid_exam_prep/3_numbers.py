sample_array = [
    int(num)
    for num in input().split()
]
avg_number = sum(sample_array) / len(sample_array)

filtered_array = list(filter(lambda x: x > avg_number, sample_array))

if filtered_array:
    sorted_array = " ".join(str(num) for num in sorted(filtered_array, reverse=True)[:5])
    print(sorted_array)
else:
    print("No")
