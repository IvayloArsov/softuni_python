window.addEventListener("load", solve);

function solve() {
  const formElement = document.querySelector("form");

  const inputStudentName = document.getElementById("student");
  const inputStudentUniversity = document.getElementById("university");
  const inputStudentScore = document.getElementById("score");

  const addButton = document.getElementById("next-btn");

  const reviewPanel = document.getElementById("preview-list");
  const finalPanel = document.getElementById("candidates-list");

  addButton.addEventListener("click", add);

  function add() {
    if (
      inputStudentName.value == "" ||
      inputStudentUniversity.value == "" ||
      inputStudentScore.value == ""
    ) {
      return;
    }

    const inputLiElement = document.createElement("li");

    inputLiElement.classList.add("application");

    const inputArticleElement = document.createElement("article");

    const pName = document.createElement("h4");
    const nameContent = inputStudentName.value;
    pName.textContent = inputStudentName.value;

    const pUniversity = document.createElement("p");
    const universityContent = inputStudentUniversity.value;
    pUniversity.textContent = `University: ${inputStudentUniversity.value}`;

    const pScore = document.createElement("p");
    const scoreContent = inputStudentScore.value;
    pScore.textContent = `Score: ${inputStudentScore.value}`;

    inputArticleElement.appendChild(pName);
    inputArticleElement.appendChild(pUniversity);
    inputArticleElement.appendChild(pScore);

    const buttonEdit = document.createElement("button");
    buttonEdit.classList.add("action-btn");
    buttonEdit.classList.add("edit");
    buttonEdit.textContent = "edit";
    buttonEdit.addEventListener("click", edit);

    const buttonApply = document.createElement("button");
    buttonApply.classList.add("action-btn");
    buttonApply.classList.add("apply");
    buttonApply.textContent = "apply";
    buttonApply.addEventListener("click", publish);

    inputLiElement.appendChild(inputArticleElement);
    inputLiElement.appendChild(buttonEdit);
    inputLiElement.appendChild(buttonApply);

    reviewPanel.appendChild(inputLiElement);
    formElement.reset();
    addButton.disabled = true;

    function edit() {
      inputStudentName.value = nameContent;
      inputStudentUniversity.value = universityContent;
      inputStudentScore.value = scoreContent;

      reviewPanel.removeChild(inputLiElement);
      addButton.disabled = false;
    }

    function publish() {
      reviewPanel.removeChild(inputLiElement);
      inputLiElement.removeChild(buttonEdit);
      inputLiElement.removeChild(buttonApply);
      finalPanel.appendChild(inputLiElement);
      addButton.disabled = false;
    }
  }
}
