function solve(inputStr, num1, num2) {
  let result;
  result = inputStr.slice(num1, num1 + num2);
  console.log(result);
}

solve("ASentence", 1, 8);
solve("SkipWord", 4, 7);
