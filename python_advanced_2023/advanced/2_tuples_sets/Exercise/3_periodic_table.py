num_inputs = int(input())
unique_elements = set()

for _ in range(num_inputs):
    info = input().split()
    unique_elements.update(info)

print("\n".join(set(unique_elements)))
