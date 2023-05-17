command1 = input()
command2 = input()

score = 0
needed_score = 20

if command1 == "Russia":
    if command2 == 'ribbon':
        score = 9.100+9.400
    if command2 == 'hoop':
        score = 9.300+9.800
    if command2 == 'rope':
        score = 9.600 + 9.000
if command1 == "Bulgaria":
    if command2 == 'ribbon':
        score = 9.600+9.400
    if command2 == 'hoop':
        score = 9.550+9.750
    if command2 == 'rope':
        score = 9.500 + 9.400
if command1 == "Italy":
    if command2 == 'ribbon':
        score = 9.500+9.200
    if command2 == 'hoop':
        score = 9.450+9.350
    if command2 == 'rope':
        score = 9.700 + 9.150

print(f"The team of {command1} get {score:.3f} on {command2}.")
print(f"{(1-(score/20))*100:.2f}%")