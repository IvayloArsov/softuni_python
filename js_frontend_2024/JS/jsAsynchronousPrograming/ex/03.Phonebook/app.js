function attachEvents() {
  const baseUrl = "http://localhost:3030/jsonstore/phonebook";
  const btnLoad = document.getElementById("btnLoad");
  const btnCreate = document.getElementById("btnCreate");
  const inputPerson = document.getElementById("person");
  const inputPhone = document.getElementById("phone");
  const phoneBookList = document.getElementById("phonebook");
  btnLoad.addEventListener("click", loadPhoneNumbers);
  btnCreate.addEventListener("click", createPhoneNumber);
  function loadPhoneNumbers() {
    fetch(baseUrl)
      .then((response) => response.json())
      .then((data) => {
        phoneBookList.innerHTML = "";
        Object.entries(data).forEach(([key, { person, phone, _id }]) => {
          const li = document.createElement("li");
          li.textContent = `${person}: ${phone}`;
          const deleteBtn = document.createElement("button");
          deleteBtn.textContent = "Delete";
          deleteBtn.addEventListener("click", () => deletePhoneNumber(_id));
          li.appendChild(deleteBtn);
          phoneBookList.appendChild(li);
        });
      });
  }
  function createPhoneNumber() {
    const person = inputPerson.value;
    const phone = inputPhone.value;

    fetch(baseUrl, {
      method: "POST",
      body: JSON.stringify({ person, phone }),
    }).then(() => {
      inputPerson.value = "";
      inputPhone.value = "";
      loadPhoneNumbers();
    });
  }

  function deletePhoneNumber(_id) {
    fetch(`${baseUrl}/${_id}`, {
      method: "DELETE",
    }).then(() => loadPhoneNumbers());
  }
}

attachEvents();
