stage = input()
ticket_grade = input()
num_tickets = int(input())
trophy_pic = input()
pic = 40
price = 0
if stage == "Final":
    if ticket_grade == 'Standard':
        price = 110.10
    if ticket_grade == 'Premium':
        price = 160.66
    if ticket_grade == 'VIP':
        price = 400
if stage == "Semi final":
    if ticket_grade == 'Standard':
        price = 75.88
    if ticket_grade == 'Premium':
        price = 125.22
    if ticket_grade == 'VIP':
        price = 300.40
if stage == "Quarter final":
    if ticket_grade == 'Standard':
        price = 55.50
    if ticket_grade == 'Premium':
        price = 105.20
    if ticket_grade == 'VIP':
        price = 118.90
sub_total = price*num_tickets
if sub_total > 4000:
    sub_total *= 0.75
    pic = 0
elif sub_total > 2500:
    sub_total *= 0.90

if trophy_pic == 'Y':
    sub_total += (pic*num_tickets)



print(f'{sub_total:.2f}')