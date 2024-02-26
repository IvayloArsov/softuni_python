function censoreWord(text, word) {
  occurances = text.split(word).length - 1;

  for (let i = 0; i < occurances; i++) {
    text = text.replace(word, "*".repeat(word.length));
  }

  console.log(text);
}

censoreWord("A small sentence with some words", "small");
censoreWord("Find the hidden word", "hidden");
