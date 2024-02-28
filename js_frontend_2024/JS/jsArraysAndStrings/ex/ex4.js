function splitAndZip(arr) {
  arr.sort((a, b) => a - b);

  const middleIndex = Math.floor(arr.length / 2);

  const firstHalf = arr.slice(0, middleIndex);
  const secondHalf = arr.slice(middleIndex).reverse();

  const zippedArray = [];
  for (let i = 0; i < Math.max(firstHalf.length, secondHalf.length); i++) {
    if (i < firstHalf.length) {
      zippedArray.push(firstHalf[i]);
    }
    if (i < secondHalf.length) {
      zippedArray.push(secondHalf[i]);
    }
  }
  return zippedArray;
}

let a = splitAndZip([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]);
console.log(a);
