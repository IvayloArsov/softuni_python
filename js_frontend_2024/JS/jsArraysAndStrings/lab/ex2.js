function reverseArr(num, arr) {
  let newArr = arr.slice(0, num).reverse();
  console.log(newArr.join(" "));
}

reverseArr(3, [10, 20, 30, 40, 50]);
reverseArr(4, [-1, 20, 99, 5]);
reverseArr(2, [66, 43, 75, 89, 47]);

function reverseArr2(num, arr) {
  let newArray = [];
  for (let i = 0; i < num; i++) {
    newArray.push(arr[i]);
  }
  console.log(newArray.reverse().join(" "));
}

reverseArr2(3, [10, 20, 30, 40, 50]);
reverseArr2(4, [-1, 20, 99, 5]);
reverseArr2(2, [66, 43, 75, 89, 47]);
