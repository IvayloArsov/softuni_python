function arrRotation(arr, rotations) {
  let temp;
  for (let i = 0; i < rotations; i++) {
    temp = arr.shift();
    arr.push(temp);
  }
  console.log(arr.join(" "));
}

arrRotation([51, 47, 32, 61, 21], 2);
arrRotation([32, 21, 61, 1], 4);
arrRotation([2, 4, 15, 31], 5);
