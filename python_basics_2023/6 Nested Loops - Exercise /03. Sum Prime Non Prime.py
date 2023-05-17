primes = 0
non_primes = 0

while True:
    command = input()

    if command == 'stop':
        break

    num = int(command)

    if num < 0:
        print('Number is negative.')
        continue
    if num < 2:
        non_primes += num
    else:
        is_prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes += num
        else:
            non_primes += num

print(f'Sum of all prime numbers is: {primes}')
print(f'Sum of all non prime numbers is: {non_primes}')