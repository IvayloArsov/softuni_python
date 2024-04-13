document.addEventListener("DOMContentLoaded", () => {
  const baseUrl = "http://localhost:3030/jsonstore/gifts/";

  const addInputBtn = document.getElementById("add-present");
  const editInputBtn = document.getElementById("edit-present");
  const loadBtn = document.getElementById("load-presents");

  const displayListElement = document.getElementById("gift-list");

  const elementGiftInput = document.getElementById("gift");
  const elementForInput = document.getElementById("for");
  const elementPriceInput = document.getElementById("price");

  loadBtn.addEventListener("click", loadElements);
  addInputBtn.addEventListener("click", addInputElement);
  editInputBtn.addEventListener("click", editInputElement);

  let currentEditingId = null;

  function loadElements() {
    fetch(baseUrl)
      .then((res) => res.json())
      .then((data) => {
        displayListElement.innerHTML = "";
        Object.keys(data).forEach((key) => {
          displayElements(data[key], key);
        });
      });
  }

  function displayElements(element) {
    const div = document.createElement("div");
    div.className = "gift-sock";
    div.innerHTML = `
    <div class="content">
                <p>${element.gift}</p>
                <p>${element.for}</p>
                <p>${element.price}</p>
              </div>
              <div class="buttons-container">
                <button class="change-btn">Change</button>
                <button class="delete-btn">Delete</button>
              </div>
    `;
    const changeBtn = div.querySelector(".change-btn");
    changeBtn.addEventListener("click", () => setupEdit(element, element._id));

    const deleteBtn = div.querySelector(".delete-btn");
    deleteBtn.addEventListener("click", () => deleteElement(element._id));

    displayListElement.appendChild(div);
  }

  function addInputElement() {
    const elementData = {
      gift: elementGiftInput.value,
      for: elementForInput.value,
      price: elementPriceInput.value,
    };

    fetch(baseUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(elementData),
    }).then(() => {
      clearForm();
      loadElements();
    });
  }

  function clearForm() {
    elementGiftInput.value = "";
    elementForInput.value = "";
    elementPriceInput.value = "";
    editInputBtn.disabled = true;
    addInputBtn.disabled = false;
    currentEditingId = null;
  }

  function deleteElement(id) {
    fetch(`${baseUrl + id}`, {
      method: "DELETE",
    }).then(() => {
      loadElements();
    });
  }

  function setupEdit(element, id) {
    elementGiftInput.value = element.gift;
    elementForInput.value = element.for;
    elementPriceInput.value = element.price;
    editInputBtn.disabled = false;
    addInputBtn.disabled = true;
    currentEditingId = id;
  }

  function editInputElement() {
    const elementData = {
      gift: elementGiftInput.value,
      for: elementForInput.value,
      price: elementPriceInput.value,
    };
    fetch(`${baseUrl + currentEditingId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(elementData),
    }).then(() => {
      clearForm();
      loadElements();
    });
  }
});
