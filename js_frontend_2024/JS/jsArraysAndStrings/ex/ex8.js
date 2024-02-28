// function pascalCaseSplitter(inputString) {
//   const resultArray = inputString.split(/(?=[A-Z])/);
//   return resultArray.join(", ");
// }

function pascalCaseSplitter(inputString) {
  let resultArray = [];
  let currentWord = "";

  for (let i = 0; i < inputString.length; i++) {
    const currentChar = inputString[i];

    if (currentChar === currentChar.toUpperCase() && i > 0) {
      resultArray.push(currentWord);
      currentWord = currentChar;
    } else {
      currentWord += currentChar;
    }
  }

  resultArray.push(currentWord);

  return resultArray.join(", ");
}

const a = pascalCaseSplitter("SplitMeIfYouCanHaHaYouCantOrYouCan");
console.log(a);
