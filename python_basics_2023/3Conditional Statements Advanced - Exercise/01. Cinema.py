projection = input()
rows = int(input())
columns = int(input())
seats = rows*columns
price = {
    'Premiere':12,
    'Normal':7.50,
    'Discount':5
}
if projection in price.keys():
    print(f'{price[projection]*seats:.2f} leva')
