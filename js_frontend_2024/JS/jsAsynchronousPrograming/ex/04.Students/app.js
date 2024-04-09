function attachEvents() {
  const baseUrl = "http://localhost:3030/jsonstore/collections/students";
  const inputFirstName = document.querySelector("input[name='firstName']");
  const inputLastName = document.querySelector("input[name='lastName']");
  const inputFacultyNumber = document.querySelector(
    "input[name='facultyNumber']"
  );
  const inputGrade = document.querySelector("input[name='grade']");
  const btnSubmit = document.getElementById("submit");
  const tableBody = document.querySelector("#results tbody");

  async function createStudent(student) {
    const response = await fetch(baseUrl, {
      method: "POST",
      body: JSON.stringify(student),
    });
    return response.json();
  }

  async function loadStudents() {
    tableBody.innerHTML = "";
    const response = await fetch(baseUrl);
    const data = await response.json();

    Object.values(data).forEach((student) => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
      <td>${student.firstName}</td>
      <td>${student.lastName}</td>
      <td>${student.facultyNumber}</td>
      <td>${student.grade}</td>
  `;
      tableBody.appendChild(tr);
    });
  }

  btnSubmit.addEventListener("click", async (event) => {
    event.preventDefault();
    const student = {
      firstName: inputFirstName.value,
      lastName: inputLastName.value,
      facultyNumber: inputFacultyNumber.value,
      grade: inputGrade.value,
    };
    await createStudent(student);
    await loadStudents();
    inputFirstName.value = "";
    inputLastName.value = "";
    inputFacultyNumber.value = "";
    inputGrade.value = "";
  });
  loadStudents();
}

attachEvents();
