function countOccurances(sentence, word) {
  let listWords = sentence.split(" ");
  let times = 0;

  for (let wordList of listWords) {
    if (wordList === word) {
      times += 1;
    }
  }
  console.log(times);
}

countOccurances("This is a word and it also is a sentence", "is");
countOccurances(
  "softuni is great place for learning new programming languages",
  "softuni"
);
