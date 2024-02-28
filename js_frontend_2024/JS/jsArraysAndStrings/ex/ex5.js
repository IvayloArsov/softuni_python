function revealWords(args, arr) {
  const wordsArray = args.split(", ");
  const wordsDict = {};
  wordsArray.forEach((element) => {
    const length = element.length;
    if (!wordsDict[length]) {
      wordsDict[length] = [];
    }
    wordsDict[length].push(element);
  });

  const resultArray = arr.split(" ").map((element) => {
    if (element.includes("*")) {
      const length = element.length;
      if (wordsDict[length] && wordsDict[length].length > 0) {
        return wordsDict[length].shift();
      }
    }
    return element;
  });

  return resultArray.join(" ");
}

const a = revealWords(
  "great, learning",
  "softuni is ***** place for ******** new programming languages"
);
const b = revealWords(
  "great",
  "softuni is ***** place for learning new programming languages"
);
console.log(a);
console.log(b);
