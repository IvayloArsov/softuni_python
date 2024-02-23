function calculator(num1, operand, num2) {
    num1 = parseFloat(num1);
    num2 = parseFloat(num2);

    switch (operand) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if (num2 === 0) {
                result = "Cannot divide by zero.";
            } else {
                result = num1 / num2;
            }
            break;
        default:
            result = '';
    }

    console.log(result.toFixed(2));
}

calculator(25.5,
    '-',
    3)