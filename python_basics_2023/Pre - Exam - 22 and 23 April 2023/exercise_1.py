people = int(input())
nights = int(input())
cards_transport = int(input())
museum_tickets = int(input())

person = nights*20 + cards_transport*1.60 + museum_tickets*6

expenses = people * (person*1.25)

print(f"{expenses:.2f}")