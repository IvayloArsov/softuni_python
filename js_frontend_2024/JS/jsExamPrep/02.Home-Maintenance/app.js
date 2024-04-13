window.addEventListener("load", solve);

function solve() {
  const place = document.getElementById("place");
  const action = document.getElementById("action");
  const person = document.getElementById("person");
  const taskList = document.getElementById("task-list");
  const doneList = document.getElementById("done-list");
  const addBtn = document.getElementById("add-btn");

  addBtn.addEventListener("click", function () {
    const li = document.createElement("li");
    li.classList.add("clean-task");
    let structureLi = `
    <article>
      <p>Place:${place.value}</p>
      <p>Action:${action.value}</p>
      <p>Person:${person.value}</p>
    </article>
    <div class="buttons">
      <button class="edit">Edit</button>
      <button class="done">Done</button>
    </div>
    `;
    li.innerHTML = structureLi;
    taskList.appendChild(li);

    place.value = "";
    action.value = "";
    person.value = "";

    const editBtn = li.querySelector(".edit");
    editBtn.addEventListener("click", function () {
      const details = li.querySelectorAll("article p");
      place.value = details[0].textContent.replace("Place: ", "");
      action.value = details[1].textContent.replace("Action: ", "");
      person.value = details[2].textContent.replace("Person: ", "");
      taskList.removeChild(li);
    });

    const doneBtn = li.querySelector(".done");
    doneBtn.addEventListener("click", function () {
      taskList.removeChild(li);
      li.querySelector(
        "div"
      ).innerHTML = `<button class="delete">Delete</button>`;
      doneList.appendChild(li);

      const deleteBtn = li.querySelector(".delete");
      deleteBtn.addEventListener("click", function () {
        doneList.removeChild(li);
      });
    });
  });
}
