function solve() {
  const inputText = document.getElementById("input").value.trim();
  const sentences = inputText.split(".").filter((sentence) => sentence.trim());

  document.getElementById("output").innerHTML = " ";

  for (let i = 0; i < sentences.length; i += 3) {
    const paragraph = document.createElement("p");
    let paragraphText = "";
    for (let j = i; j < Math.min(i + 3, sentences.length); j++) {
      paragraphText += sentences[j] + ". ";
    }
    paragraph.textContent = paragraphText.trim();
    document.getElementById("output").appendChild(paragraph);
  }
}
