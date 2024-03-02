function solve(num1, num2, num3) {
  function sum(num1, num2) {
    const result = num1 + num2;
    return result;
  }

  function subtract(result, num3) {
    return result - num3;
  }

  const sumResult = sum(num1, num2);
  const finalResult = subtract(sumResult, num3);

  return finalResult;
}

console.log(solve(23, 6, 10));
console.log(solve(1, 17, 30));
console.log(solve(42, 58, 100));
