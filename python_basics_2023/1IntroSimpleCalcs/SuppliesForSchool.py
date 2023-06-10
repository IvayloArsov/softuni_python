pens = 5.80
markers = 7.20
cleaning_mats = 1.20

num_pens = int(input())*pens
num_markers = int(input()) * markers
num_cleaning = int(input()) * cleaning_mats
discount = 1- (int(input())/100)

money_needed = (num_cleaning+num_markers+num_pens)*discount
print(money_needed)