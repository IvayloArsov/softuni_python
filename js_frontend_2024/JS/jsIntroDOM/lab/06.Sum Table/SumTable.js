function sumTable() {
  const tableRowsElements = document.querySelectorAll("table tr");
  let totalSum = 0;

  for (let index = 1; index < tableRowsElements.length; index++) {
    const cells = tableRowsElements[index].children;
    const cellPrice = Number(cells[1].textContent);
    totalSum += cellPrice;
  }
  document.getElementById("sum").textContent = totalSum;
}
