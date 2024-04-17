window.addEventListener("load", solve);

function solve() {
  const formElement = document.querySelector("form");

  const inputPlayerName = document.getElementById("player");
  const inputPlayerScore = document.getElementById("score");
  const inputPlayerRound = document.getElementById("round");

  const addButton = document.getElementById("add-btn");
  const clearButton = document.querySelector(".clear");

  const reviewPanel = document.getElementById("sure-list");
  const scoreboardPanel = document.getElementById("scoreboard-list");

  addButton.addEventListener("click", add);

  function add() {
    if (
      inputPlayerName.value == "" ||
      inputPlayerScore.value == "" ||
      inputPlayerRound.value == ""
    ) {
      return;
    }

    const inputLiElement = document.createElement("li");
    inputLiElement.classList.add("dart-item");

    const inputArticleElement = document.createElement("article");

    const pName = document.createElement("p");
    const nameContent = inputPlayerName.value;
    pName.textContent = inputPlayerName.value;

    const pScore = document.createElement("p");
    const scoreContent = inputPlayerScore.value;
    pScore.textContent = `Score: ${inputPlayerScore.value}`;

    const pRound = document.createElement("p");
    const roundContent = inputPlayerRound.value;
    pRound.textContent = `Round: ${inputPlayerRound.value}`;

    inputArticleElement.appendChild(pName);
    inputArticleElement.appendChild(pScore);
    inputArticleElement.appendChild(pRound);

    const buttonEdit = document.createElement("button");
    buttonEdit.classList.add("btn");
    buttonEdit.classList.add("edit");
    buttonEdit.textContent = "edit";
    buttonEdit.addEventListener("click", edit);

    const buttonOk = document.createElement("button");
    buttonOk.classList.add("btn");
    buttonOk.classList.add("ok");
    buttonOk.textContent = "ok";
    buttonOk.addEventListener("click", publish);

    inputLiElement.appendChild(inputArticleElement);
    inputLiElement.appendChild(buttonEdit);
    inputLiElement.appendChild(buttonOk);

    reviewPanel.appendChild(inputLiElement);
    formElement.reset();
    addButton.disabled = true;

    function edit() {
      inputPlayerName.value = nameContent;
      inputPlayerScore.value = scoreContent;
      inputPlayerRound.value = roundContent;

      reviewPanel.removeChild(inputLiElement);
      addButton.disabled = false;
    }

    function publish() {
      reviewPanel.removeChild(inputLiElement);
      inputLiElement.removeChild(buttonEdit);
      inputLiElement.removeChild(buttonOk);
      scoreboardPanel.appendChild(inputLiElement);
      addButton.disabled = false;

      clearButton.addEventListener("click", clear);

      function clear() {
        location.reload();
      }
    }
  }
}
