document.addEventListener("DOMContentLoaded", () => {
  const baseURL = `http://localhost:3030/jsonstore/tasks/`;

  const inputForm = document.querySelector("form");
  const contentDisplayDiv = document.getElementById("list");

  const loadButton = document.getElementById("load-vacations");
  const addButton = document.getElementById("add-vacation");
  const editButton = document.getElementById("edit-vacation");

  const inputName = document.getElementById("name");
  const inputDays = document.getElementById("num-days");
  const inputDate = document.getElementById("from-date");

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

  function displayContent(content) {
    const div = document.createElement("div");
    div.className = "container";
    div.innerHTML = `
        <h2>${content.name}</h2>
        <h3>${content.date}</h3>
        <h3>${content.days}</h3>
        <button class="change-btn">Change</button>
        <button class="done-btn">Done</button>
        `;

    const changeBtn = div.querySelector(".change-btn");
    const doneBtn = div.querySelector(".done-btn");
    changeBtn.addEventListener("click", () => setupEdit(content, content._id));
    doneBtn.addEventListener("click", () => deleteContent(content._id));
    contentDisplayDiv.appendChild(div);
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
      days: inputDays.value,
      date: inputDate.value,
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
    inputDays.value = content.days;
    inputDate.value = content.date;
    editButton.disabled = false;
    addButton.disabled = true;
    currentEditingID = id;
  }

  function editContent() {
    const contentData = {
      name: inputName.value,
      days: inputDays.value,
      date: inputDate.value,
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
