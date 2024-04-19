window.addEventListener("load", solve);

function solve() {
  const addButton = document.getElementById("add-btn");
  const nameInput = document.getElementById("name");
  const phoneInput = document.getElementById("phone");
  const categorySelect = document.getElementById("category");
  const checkList = document.getElementById("check-list");
  const contactList = document.getElementById("contact-list");

  addButton.addEventListener("click", function () {
    const name = nameInput.value.trim();
    const phone = phoneInput.value.trim();
    const category = categorySelect.value;

    if (name === "" || phone === "" || category === "") {
      return;
    }

    const contactInfo = { name, phone, category };

    const li = document.createElement("li");
    const article = document.createElement("article");
    const pName = document.createElement("p");
    const pPhone = document.createElement("p");
    const pCategory = document.createElement("p");
    const divButtons = document.createElement("div");
    const editButton = document.createElement("button");
    const saveButton = document.createElement("button");

    pName.textContent = `name:${contactInfo.name}`;
    pPhone.textContent = `phone:${contactInfo.phone}`;
    pCategory.textContent = `category:${contactInfo.category}`;

    divButtons.className = "buttons";
    editButton.className = "edit-btn";
    saveButton.className = "save-btn";

    article.appendChild(pName);
    article.appendChild(pPhone);
    article.appendChild(pCategory);
    divButtons.appendChild(editButton);
    divButtons.appendChild(saveButton);
    li.appendChild(article);
    li.appendChild(divButtons);
    checkList.appendChild(li);

    nameInput.value = "";
    phoneInput.value = "";
    categorySelect.value = "";

    editButton.addEventListener("click", function () {
      nameInput.value = contactInfo.name;
      phoneInput.value = contactInfo.phone;
      categorySelect.value = contactInfo.category;
      checkList.removeChild(li);
    });

    saveButton.addEventListener("click", function () {
      const deleteButton = document.createElement("button");
      deleteButton.className = "del-btn";

      deleteButton.addEventListener("click", function () {
        contactList.removeChild(li);
      });

      contactList.appendChild(li);
      divButtons.innerHTML = "";
      li.appendChild(deleteButton);
      li.removeChild(divButtons);
    });
  });
}
