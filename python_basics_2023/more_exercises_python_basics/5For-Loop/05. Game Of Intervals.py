nums = int(input())
score = 0
invalids = 0
ones = 0
tens = 0
twenties = 0
thirties = 0
forties = 0
for n in range(0, nums):
    num = int(input())
    if num < 0 or num > 50:
        score /= 2
        invalids += 1
    elif num >= 40:
        score += 100
        forties += 1
    elif num >= 30:
        score += 50
        thirties += 1
    elif num >= 20:
        score += num * 0.4
        twenties += 1
    elif num >= 10:
        score += num * 0.3
        tens += 1
    elif num >= 0:
        score += num * 0.2
        ones += 1
print(f'{score:.2f}')
print(f'From 0 to 9: {ones / nums * 100:.2f}%')
print(f'From 10 to 19: {tens / nums * 100:.2f}%')
print(f'From 20 to 29: {twenties / nums * 100:.2f}%')
print(f'From 30 to 39: {thirties / nums * 100:.2f}%')
print(f'From 40 to 50: {forties / nums * 100:.2f}%')
print(f'Invalid numbers: {invalids / nums * 100:.2f}%')
