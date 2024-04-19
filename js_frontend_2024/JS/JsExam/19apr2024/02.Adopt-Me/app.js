window.addEventListener("load", solve);

function solve() {
  const formElement = document.querySelector("form");

  const inputAnimalType = document.getElementById("type");
  const inputAnimalAge = document.getElementById("age");
  const inputAnimalGender = document.getElementById("gender");

  const adoptButton = document.getElementById("adopt-btn");

  const reviewPanel = document.getElementById("adoption-info");
  const scoreboardPanel = document.getElementById("adopted-list");

  adoptButton.addEventListener("click", adopt);

  function adopt() {
    if (
      inputAnimalType.value == "" ||
      inputAnimalAge.value == "" ||
      inputAnimalGender.value == ""
    ) {
      return;
    }

    const inputLiElement = document.createElement("li");
    const inputArticleElement = document.createElement("article");

    const pType = document.createElement("p");
    const typeContent = inputAnimalType.value;
    pType.textContent = `Pet:${inputAnimalType.value}`;

    const pAge = document.createElement("p");
    const ageContent = inputAnimalAge.value;
    pAge.textContent = `Gender:${inputAnimalGender.value}`;

    const pGender = document.createElement("p");
    const roundContent = inputAnimalGender.value;
    pGender.textContent = `Age:${inputAnimalAge.value}`;

    inputArticleElement.appendChild(pType);
    inputArticleElement.appendChild(pAge);
    inputArticleElement.appendChild(pGender);

    const buttonEdit = document.createElement("button");
    buttonEdit.classList.add("edit-btn");
    buttonEdit.textContent = "Edit";
    buttonEdit.addEventListener("click", edit);

    const buttonDone = document.createElement("button");
    buttonDone.classList.add("done-btn");
    buttonDone.textContent = "Done";
    buttonDone.addEventListener("click", publish);

    const buttonsDiv = document.createElement("div");
    buttonsDiv.classList.add("buttons");
    buttonsDiv.appendChild(buttonEdit);
    buttonsDiv.appendChild(buttonDone);

    inputLiElement.appendChild(inputArticleElement);
    inputLiElement.appendChild(buttonsDiv);

    reviewPanel.appendChild(inputLiElement);
    formElement.reset();
    adoptButton.disabled = true;

    function edit() {
      inputAnimalType.value = typeContent;
      inputAnimalAge.value = ageContent;
      inputAnimalGender.value = roundContent;

      reviewPanel.removeChild(inputLiElement);
      adoptButton.disabled = false;
    }

    function publish() {
      reviewPanel.removeChild(inputLiElement);
      inputLiElement.removeChild(buttonsDiv);

      const clearButton = document.createElement("button");
      clearButton.textContent = "Clear";
      clearButton.classList.add("clear-btn");

      inputLiElement.appendChild(clearButton);
      scoreboardPanel.appendChild(inputLiElement);
      adoptButton.disabled = false;

      clearButton.addEventListener("click", clear);

      function clear() {
        inputLiElement.remove();
      }
    }
  }
}
