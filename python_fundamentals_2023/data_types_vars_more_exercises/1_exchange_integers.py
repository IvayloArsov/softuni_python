num1 = int(input())
num2 = int(input())
print(f"Before:\n"
      f"a = {num1}\n"
      f"b = {num2}\n", end="")
num1, num2 = num2, num1
print(f"After:\n"
      f"a = {num1}\n"
      f"b = {num2}")