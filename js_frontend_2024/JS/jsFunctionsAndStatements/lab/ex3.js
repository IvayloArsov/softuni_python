function repeatString(string, repeats) {
  let newString = "";
  for (let i = 0; i < repeats; i++) {
    newString += string;
  }
  return newString;
}

console.log(repeatString("abc", 3));
console.log(repeatString("String", 2));
