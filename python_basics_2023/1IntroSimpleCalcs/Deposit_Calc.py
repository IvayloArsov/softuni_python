Deposit = float(input())
LenDeposit = int(input())
AnnualInterest = float(input())/100
Interest = Deposit + LenDeposit*((Deposit*AnnualInterest)/12)

print(Interest)