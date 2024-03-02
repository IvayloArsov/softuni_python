function getSmallestNum(args) {
  const nums = [args];
  let smallestNum = +Infinity;
  for (const num of nums) {
    if (num < smallestNum) {
      smallestNum = num;
    }
  }
  return smallestNum;
}

console.log(getSmallestNum(2, 5, 3));
