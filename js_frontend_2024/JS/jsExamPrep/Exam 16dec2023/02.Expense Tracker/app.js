window.addEventListener("load", solve);

function solve() {
  const expenseType = document.getElementById("expense");
  const expenseAmount = document.getElementById("amount");
  const expenseDate = document.getElementById("date");

  const previewListElement = document.getElementById("preview-list");
  const expensesListElement = document.getElementById("expenses-list");

  const deleteExpenseButton = document.querySelector(".delete");
  const formElement = document.querySelector("form");

  const addInputButton = document.getElementById("add-btn");
  addInputButton.addEventListener("click", publish);

  function publish() {
    if (
      expenseType.value == "" ||
      expenseAmount.value == "" ||
      expenseDate.value == ""
    ) {
      return;
    }

    const li = document.createElement("li");
    li.classList.add("expense-item");

    const article = document.createElement("article");

    const pType = document.createElement("p");
    const typeContent = expenseType.value;
    pType.textContent = `Type: ${expenseType.value}`;

    const pAmount = document.createElement("p");
    const amountContent = expenseAmount.value;
    pAmount.textContent = `Amount: ${expenseAmount.value}$`;

    const pDate = document.createElement("p");
    const dateContent = expenseDate.value;
    pDate.textContent = `Date: ${expenseDate.value}`;

    article.appendChild(pType);
    article.appendChild(pAmount);
    article.appendChild(pDate);

    const buttonEdit = document.createElement("button");
    buttonEdit.classList.add("btn");
    buttonEdit.classList.add("edit");
    buttonEdit.textContent = "edit";
    buttonEdit.addEventListener("click", edit);

    const buttonOK = document.createElement("button");
    buttonOK.classList.add("btn");
    buttonOK.classList.add("ok");
    buttonOK.textContent = "ok";
    buttonOK.addEventListener("click", add);

    const liButtonsDiv = document.createElement("div");

    liButtonsDiv.classList.add("buttons");
    liButtonsDiv.appendChild(buttonEdit);
    liButtonsDiv.appendChild(buttonOK);

    li.appendChild(article);
    li.appendChild(liButtonsDiv);

    previewListElement.appendChild(li);
    formElement.reset();
    addInputButton.disabled = true;

    function edit() {
      expenseType.value = typeContent;
      expenseAmount.value = amountContent;
      expenseDate.value = dateContent;

      previewListElement.removeChild(li);
      addInputButton.disabled = false;
    }

    function add() {
      previewListElement.removeChild(li);
      li.removeChild(liButtonsDiv);
      expensesListElement.appendChild(li);
      addInputButton.disabled = false;

      deleteExpenseButton.addEventListener("click", clear);

      function clear() {
        location.reload();
      }
    }
  }
}
