function carWash(arr) {
  let status = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === "soap") {
      status += 10;
    } else if (arr[i] === "water") {
      status *= 1.2;
    } else if (arr[i] === "vacuum cleaner") {
      status *= 1.25;
    } else if (arr[i] === "mud") {
      status *= 0.9;
    }
  }
  console.log(`The car is ${status.toFixed(2)}% clean.`);
}

carWash(["soap", "soap", "vacuum cleaner", "mud", "soap", "water"]);
carWash(["soap", "water", "mud", "mud", "water", "mud", "vacuum cleaner"]);
