function extractOddOccurrences(sentence) {
  const words = sentence.toLowerCase().split(" ");

  const wordCount = {};
  for (const word of words) {
    wordCount[word] = (wordCount[word] || 0) + 1;
  }

  const oddOccurrences = [];
  for (const word of words) {
    if (wordCount[word] % 2 !== 0 && !oddOccurrences.includes(word)) {
      oddOccurrences.push(word);
    }
  }

  return oddOccurrences.join(" ");
}

console.log(extractOddOccurrences("Java C# Php PHP Java PhP 3 C# 3 1 5 C#"));
console.log(extractOddOccurrences("Cake IS SWEET is Soft CAKE sweet Food"));
