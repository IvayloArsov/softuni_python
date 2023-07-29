import re

pattern = re.compile(
    r"%(?P<customer>[A-Z][a-z]+)%([^\|\$\%\.]*)"
    r"<(?P<product>\w+)>([^\|\$\%\.]*)"
    r"\|(?P<quantity>\d+)\|([^\|\$\%\.]*)"
    r"(?P<price>[1-9]+[.0-9]*)\$"
)

total_income = 0

input_string = input()
while input_string != "end of shift":
    matches = re.finditer(pattern, input_string)
    for match in matches:
        subtotal = float(match["quantity"]) * float(match["price"])
        total_income += subtotal
        print(f"{match['customer']}: {match['product']} - {subtotal:.2f}")

    input_string = input()
print(f"Total income: {total_income:.2f}")
