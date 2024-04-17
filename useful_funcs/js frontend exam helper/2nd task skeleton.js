
//COMMENT THIS NEXT LINE WHEN SUBMITTING YOUR WORK
window.addEventListener("load", solve);


function solve() {
//Check if form element is selected properly
  const formElement = document.querySelector("form");

//input fields = change depending on IDs
  const inputPlayerName = document.getElementById("player");
  const inputPlayerScore = document.getElementById("score");
  const inputPlayerRound = document.getElementById("round");

// buttons - change if IDs are different
  const addButton = document.getElementById("add-btn");
  const clearButton = document.querySelector(".clear");

//output divs - change if IDs are different
  const reviewPanel = document.getElementById("sure-list");
  const scoreboardPanel = document.getElementById("scoreboard-list");

  addButton.addEventListener("click", add);

  function add() {
  //change variable names depending on naming above, this checks for null entries
    if (
      inputPlayerName.value == "" ||
      inputPlayerScore.value == "" ||
      inputPlayerRound.value == ""
    ) {
      return;
    }

    const inputLiElement = document.createElement("li");
    //change id
    inputLiElement.classList.add("dart-item");

//next lines depend on format expected, CHECK IT SUPER CAREFULLY. 
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

//check vars
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

//check if buttons are in separate div, if yes - make a div above this and appendChild the div to the article
    inputLiElement.appendChild(inputArticleElement);
    inputLiElement.appendChild(buttonEdit);
    inputLiElement.appendChild(buttonOk);

//check if reset works, and if buttons are disabled/enabled
    reviewPanel.appendChild(inputLiElement);
    formElement.reset();
    addButton.disabled = true;
    
    
	//check var names super carefully here, button if needs to be disabled
    function edit() {
      inputPlayerName.value = nameContent;
      inputPlayerScore.value = scoreContent;
      inputPlayerRound.value = roundContent;

      reviewPanel.removeChild(inputLiElement);
      addButton.disabled = false;
    }
    
    //check if publish panel is selected
    //remove SUPER CAREFULLY the divs for buttons or the buttons themselves. CAREFUL with the expected format!!!

    function publish() {
      reviewPanel.removeChild(inputLiElement);
      inputLiElement.removeChild(buttonEdit);
      inputLiElement.removeChild(buttonOk);
      scoreboardPanel.appendChild(inputLiElement);
      addButton.disabled = false;

//this should work
      clearButton.addEventListener("click", clear);

	// check if they want reload or deleting each element, this reload was on the old exams
      function clear() {
        location.reload();
      }
    }
  }
}

