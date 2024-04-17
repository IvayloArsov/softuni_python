document.addEventListener("DOMContentLoaded", () => {
  const baseURL = `http://localhost:3030/jsonstore/tasks/`;
  const inputForm = document.querySelector("#form form");
  const contentDisplayDiv = document.getElementById("list");

  const loadButton = document.getElementById("load-history");
  const addButton = document.getElementById("add-weather");
  const editButton = document.getElementById("edit-weather");

  const inputLocation = document.getElementById("location");
  const inputTemperature = document.getElementById("temperature");
  const inputDate = document.getElementById("date");

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
    <h2>${content.location}</h2>
    <h3>${content.date}</h3>
    <h3 id="celsius">${content.temperature}</h3>
    <div id="buttons-container">
        <button class="change-btn">Change</button>
        <button class="delete-btn">Delete</button>
    </div>
    `;
    const changeBtn = div.querySelector(".change-btn");
    const deleteBtn = div.querySelector(".delete-btn");
    changeBtn.addEventListener("click", () => setupEdit(content, content._id));
    deleteBtn.addEventListener("click", () => deleteContent(content._id));
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
      location: inputLocation.value,
      temperature: inputTemperature.value,
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
    inputLocation.value = content.location;
    inputTemperature.value = content.temperature;
    inputDate.value = content.date;
    editButton.disabled = false;
    addButton.disabled = true;
    currentEditingID = id;
  }

  function editContent() {
    const contentData = {
      location: inputLocation.value,
      temperature: inputTemperature.value,
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
