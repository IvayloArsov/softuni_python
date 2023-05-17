import math

tennis_racquet = float(input())
num_racquets = int(input())
num_sneakers = int(input())


total_sum_racquets = tennis_racquet* num_racquets
total_sum_sneakers = num_sneakers * (tennis_racquet/6)

__sum = (total_sum_racquets + total_sum_sneakers)*1.2

print(f"Price to be paid by Djokovic {math.floor(__sum * (1 / 8))}")
print(f"Price to be paid by sponsors {math.ceil(__sum *( 7 / 8))}")