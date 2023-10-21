N = int(input())

start_index = 0
current_petrol = 0
total_petrol = 0
distance = 0

for i in range(N):
    petrol, dist = map(int, input().split())
    current_petrol += petrol - dist
    total_petrol += petrol
    distance += dist

    if current_petrol < 0:
        start_index = i + 1
        current_petrol = 0

print(start_index)
