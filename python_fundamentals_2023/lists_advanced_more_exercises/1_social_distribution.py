pop = [int(num) for num in input().split(", ")]
min_wealth = int(input())

if min_wealth > sum(pop) / len(pop):
    print("No equal distribution possible")
    exit()
while any(x < min_wealth for x in pop):
    max_number, number_to_change = max(pop), min(pop)
    index_max, index_min = pop.index(max_number), pop.index(number_to_change)
    added_value = min_wealth - number_to_change
    pop[index_max] -= added_value
    pop[index_min] += added_value

print(pop)