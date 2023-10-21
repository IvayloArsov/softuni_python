input_lines = int(input())
longest_intersection = set()

for _ in range(input_lines):
    first, second = input().split("-")
    first_start, first_end = first.split(",")
    first_pair = set(range(int(first_start), int(first_end)+1))
    second_start, second_end = second.split(",")
    second_pair = set(range(int(second_start), int(second_end)+1))
    current_intersection = first_pair & second_pair

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

# for _ in range(input_lines):
#     first, second = input().split("-")
#     first_start, first_end = map(int, first.split(","))
#     second_start, second_end = map(int, second.split(","))
#
#     intersection_start = max(first_start, second_start)
#     intersection_end = min(first_end, second_end)
#
#     if intersection_start <= intersection_end:
#         current_intersection = set(range(intersection_start, intersection_end + 1))
#
#         if len(current_intersection) > len(longest_intersection):
#             longest_intersection = current_intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")