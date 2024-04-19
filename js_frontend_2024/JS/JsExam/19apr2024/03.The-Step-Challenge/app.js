document.addEventListener("DOMContentLoaded", () => {
  const baseURL = `http://localhost:3030/jsonstore/records/`;

  const inputForm = document.querySelector("form");
  const contentDisplayDiv = document.getElementById("list");

  const loadButton = document.getElementById("load-records");
  const addButton = document.getElementById("add-record");
  const editButton = document.getElementById("edit-record");

  const inputName = document.getElementById("p-name");
  const inputSteps = document.getElementById("steps");
  const inputCalories = document.getElementById("calories");

  loadButton.addEventListener("click", loadContent);
  addButton.addEventListener("click", addContent);
  editButton.addEventListener("click", editContent);

  let currentEditingID = null;

  function loadContent() {
    fetch(baseURL)
      .then((response) => response.json())
      .then((data) => {
        contentDisplayDiv.innerHTML = "";
        Object.keys(data).forEach((key) => {
          displayContent(data[key], key);
        });
      });
  }

  function displayContent(content, id) {
    const li = document.createElement("li");
    li.className = "record";
    li.innerHTML = `
        <div class="info">
            <p>${content.name}</p>
            <p>${content.steps}</p>
            <p>${content.calories}</p>
        </div>
        <div id="btn-wrapper">
            <button class="change-btn">Change</button>
            <button class="delete-btn">Delete</button>
        </div>
        `;

    const changeBtn = li.querySelector(".change-btn");
    const deleteBtn = li.querySelector(".delete-btn");
    changeBtn.addEventListener("click", () => setupEdit(content, content._id));
    deleteBtn.addEventListener("click", () => deleteContent(content._id));
    contentDisplayDiv.appendChild(li);
  }

  function clearForm() {
    inputForm.reset();
    editButton.disabled = true;
    addButton.disabled = false;
    currentEditingID = null;
  }

  function addContent() {
    const contentData = {
      name: inputName.value,
      steps: inputSteps.value,
      calories: inputCalories.value,
    };

    fetch(baseURL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(contentData),
    }).then(() => {
      clearForm();
      loadContent();
    });
  }

  function setupEdit(content, id) {
    inputName.value = content.name;
    inputSteps.value = content.steps;
    inputCalories.value = content.calories;
    editButton.disabled = false;
    addButton.disabled = true;
    currentEditingID = id;
  }

  function editContent() {
    const contentData = {
      name: inputName.value,
      steps: inputSteps.value,
      calories: inputCalories.value,
    };

    fetch(`${baseURL + currentEditingID}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(contentData),
    }).then(() => {
      clearForm();
      loadContent();
    });
  }

  function deleteContent(id) {
    fetch(`${baseURL + id}`, {
      method: "DELETE",
    }).then(() => {
      loadContent();
    });
  }
});
