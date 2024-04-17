document.addEventListener("DOMContentLoaded", () => {
  const baseURL = `http://localhost:3030/jsonstore/tasks/`;
  const mealsList = document.getElementById("list");
  const inputForm = document.querySelector("#form form");

  const loadButton = document.getElementById("load-meals");
  const addButton = document.getElementById("add-meal");
  const editButton = document.getElementById("edit-meal");

  const mealFoodInput = document.getElementById("food");
  const mealTimeInput = document.getElementById("time");
  const mealCaloriesInput = document.getElementById("calories");

  loadButton.addEventListener("click", loadContent);
  addButton.addEventListener("click", addMeal);
  editButton.addEventListener("click", editMeal);

  let currentEditingID = null;

  function loadContent() {
    fetch(baseURL)
      .then((response) => response.json())
      .then((data) => {
        mealsList.innerHTML = "";
        Object.keys(data).forEach((key) => {
          displayMeal(data[key], key);
        });
      });
  }

  function displayMeal(meal) {
    const div = document.createElement("div");
    div.className = "meal";
    div.innerHTML = `
    <h2>${meal.food}</h2>
    <h3>${meal.time}</h3>
    <h3>${meal.calories}</h3>
    <div id="meal-buttons">
        <button class="change-meal">Change</button>
        <button class="delete-meal">Delete</button>
    </div>
    `;
    const changeBtn = div.querySelector(".change-meal");
    const deleteBtn = div.querySelector(".delete-meal");
    changeBtn.addEventListener("click", () => setupEdit(meal, meal._id));
    deleteBtn.addEventListener("click", () => deleteMeal(meal._id));
    mealsList.appendChild(div);
  }
  function clearForm() {
    inputForm.reset();
    editButton.disabled = true;
    addButton.disabled = false;
    currentEditingID = null;
  }

  function addMeal() {
    const mealData = {
      food: mealFoodInput.value,
      calories: mealCaloriesInput.value,
      time: mealTimeInput.value,
    };
    fetch(baseURL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(mealData),
    }).then(() => {
      clearForm();
      loadContent();
    });
  }

  function setupEdit(meal, id) {
    mealFoodInput.value = meal.food;
    mealTimeInput.value = meal.time;
    mealCaloriesInput.value = meal.calories;
    editButton.disabled = false;
    addButton.disabled = true;
    currentEditingID = id;
  }

  function editMeal() {
    const mealData = {
      food: mealFoodInput.value,
      calories: mealCaloriesInput.value,
      time: mealTimeInput.value,
    };
    fetch(`${baseURL + currentEditingID}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(mealData),
    }).then(() => {
      clearForm();
      loadContent();
    });
  }
  function deleteMeal(currentEditingID) {
    let id = currentEditingID;
    fetch(`${baseURL + id}`, {
      method: "DELETE",
    }).then(() => {
      loadContent();
    });
  }
});
