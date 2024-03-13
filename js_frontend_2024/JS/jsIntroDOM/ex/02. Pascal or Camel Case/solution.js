function solve() {
  let input = document.getElementById("text").value;
  let currentCase = document.getElementById("naming-convention").value;
  let result = "";

  if (currentCase === "Camel Case") {
    let words = input.toLowerCase().split(" ");
    for (let i = 0; i < words.length; i++) {
      if (i !== 0) {
        result += words[i][0].toUpperCase() + words[i].slice(1);
      } else {
        result += words[i];
      }
    }
  } else if (currentCase === "Pascal Case") {
    let words = input.toLowerCase().split(" ");
    for (let i = 0; i < words.length; i++) {
      result += words[i][0].toUpperCase() + words[i].slice(1);
    }
  } else {
    result = "Error!";
  }

  document.getElementById("result").innerText = result;
}
