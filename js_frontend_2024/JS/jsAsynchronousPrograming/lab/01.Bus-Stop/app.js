function getInfo() {
  document.getElementById("stopName").textContent = "";
  document.getElementById("buses").innerHTML = "";

  let stopId = document.getElementById("stopId").value;

  fetch(`http://localhost:3030/jsonstore/bus/businfo/${stopId}`)
    .then((response) => {
      response.json();
    })
    .then((data) => {
      document.getElementById("stopName").textContent = data.name;

      for (let busId in data.buses) {
        let time = data.buses[busId];
        let listItem = document.createElement("li");
        listItem.textContent = `Bus ${busId} arrives in ${time} minutes`;
        document.getElementById("buses").appendChild(listItem);
      }
    })
    .catch(() => {
      document.getElementById("stopName").textContent = "Error";
    });
}
