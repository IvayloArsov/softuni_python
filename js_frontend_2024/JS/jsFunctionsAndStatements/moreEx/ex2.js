function modifyNumber(number) {
  let num = number.toString();
  let sum = 0;
  let length = num.length;

  for (let i = 0; i < length; i++) {
    sum += parseInt(num[i]);
  }

  while (sum / length < 5) {
    num += "9";
    sum += 9;
    length++;
  }

  console.log(num);
}

modifyNumber(101);
modifyNumber(5835);
