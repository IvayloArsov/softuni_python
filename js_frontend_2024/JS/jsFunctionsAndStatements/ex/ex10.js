function calculateFactorialDivision(num1, num2) {
  function factorial(n) {
    return n === 0 || n === 1 ? 1 : n * factorial(n - 1);
  }
  const factorialNum1 = factorial(num1);
  const factorialNum2 = factorial(num2);

  const result = factorialNum1 / factorialNum2;
  console.log(result.toFixed(2));
}

calculateFactorialDivision(5, 2);
