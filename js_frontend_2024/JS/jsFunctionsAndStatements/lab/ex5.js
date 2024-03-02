function simpleCalculator(numOne, numTwo, operator) {
  const operators = {
    multiply: (a, b) => a * b,
    divide: (a, b) => a / b,
    add: (a, b) => a + b,
    subtract: (a, b) => a - b,
  };
  const selectedOperator = operators[operator];

  return selectedOperator(numOne, numTwo);
}

console.log(simpleCalculator(5, 5, "multiply"));
console.log(simpleCalculator(40, 8, "divide"));
console.log(simpleCalculator(12, 19, "add"));
