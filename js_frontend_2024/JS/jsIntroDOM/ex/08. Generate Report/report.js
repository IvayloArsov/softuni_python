function generateReport() {
  let selectedColumns = [];

  let checkboxes = document.querySelectorAll('input[type="checkbox"]');
  for (let i = 0; i < checkboxes.length; i++) {
    if (checkboxes[i].checked) {
      selectedColumns.push(checkboxes[i].name);
    }
  }

  let jsonData = [];
  let rows = document.querySelectorAll("tbody tr");
  for (let i = 0; i < rows.length; i++) {
    let rowData = {};
    let cells = rows[i].querySelectorAll("td");
    for (let j = 0; j < cells.length; j++) {
      if (selectedColumns.includes(checkboxes[j].name)) {
        rowData[selectedColumns[selectedColumns.indexOf(checkboxes[j].name)]] =
          cells[j].textContent.trim();
      }
    }
    jsonData.push(rowData);
  }

  let jsonString = JSON.stringify(jsonData, null, 2);
  let outputTextarea = document.getElementById("output");
  outputTextarea.value = jsonString;
}
