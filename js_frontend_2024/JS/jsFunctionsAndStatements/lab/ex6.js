function signCheck(numOne, numTwo, numThree) {
  const negativeCount = [numOne, numTwo, numThree].filter(
    (num) => num < 0
  ).length;
  return negativeCount % 2 === 0 ? "Positive" : "Negative";
}

console.log(signCheck(-5, 1, 1));
