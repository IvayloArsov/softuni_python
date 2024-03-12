function trackWordsOccurance(input) {
  const [wordsToFind, ...words] = input;
  const wordsToFindArray = wordsToFind.split(" ");
  const wordCounts = {};

  wordsToFindArray.forEach((word) => {
    wordCounts[word] = 0;
  });

  words.forEach((word) => {
    if (wordsToFindArray.includes(word)) {
      wordCounts[word]++;
    }
  });

  const sortedWordCounts = Object.entries(wordCounts).sort(
    (a, b) => b[1] - a[1]
  );
  sortedWordCounts.forEach(([word, count]) => {
    console.log(`${word} - ${count}`);
  });
}

trackWordsOccurance([
  "this sentence",
  "In",
  "this",
  "sentence",
  "you",
  "have",
  "to",
  "count",
  "the",
  "occurrences",
  "of",
  "the",
  "words",
  "this",
  "and",
  "sentence",
  "because",
  "this",
  "is",
  "your",
  "task",
]);
