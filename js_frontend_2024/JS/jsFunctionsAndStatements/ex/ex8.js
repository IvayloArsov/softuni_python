function checkPerfectNumber(num) {
  let divisorsSum = 0;

  for (let i = 0; i < num; i++) {
    if (num % i === 0) {
      divisorsSum += i;
    }
  }
  const result = divisorsSum === num;
  return result ? "We have a perfect number!" : " It's not so perfect.";
}
