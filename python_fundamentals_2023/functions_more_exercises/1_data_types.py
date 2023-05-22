user_operand = input()
user_data= input()


def calculations_(operand, data):
    if operand == "int":
        return int(data)*2
    elif operand == 'real':
        return f"{float(data) * 1.50:.2f}"
    elif operand == 'string':
        return f"${data}$"


print(calculations_(user_operand, user_data))