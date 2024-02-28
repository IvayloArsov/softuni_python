function strSubstr(word, text) {
  const arr = text.split(" ").map((element) => element.toLowerCase());

  for (const element of arr) {
    if (word === element) {
      console.log(word);
      return;
    }
  }

  console.log(`${word} not found!`);
}

strSubstr("javascript", "JavaScript is the best programming language");
console.log("\n");
strSubstr("python", "JavaScript is the best programming language");
