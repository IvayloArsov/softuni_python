def order(item, quantity):
    result = None
    if item == 'coffee':
        result = quantity * 1.50
    elif item == 'water':
        result = quantity * 1.00
    elif item == 'coke':
        result = quantity * 1.40
    elif item == 'snacks':
        result = quantity * 2.00
    return result


item = input()
quantity = int(input())
print(f"{order(item, quantity):.2f}")