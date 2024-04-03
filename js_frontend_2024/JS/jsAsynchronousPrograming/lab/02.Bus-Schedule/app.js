function solve() {
  const baseURL = "http://localhost:3030/jsonstore/bus/schedule/";
  let infoBox = document.querySelector(".info");
  let departButton = document.getElementById("depart");
  let arriveButton = document.getElementById("arrive");

  let currentStopId = "depot";
  let nextStop = "";

  async function depart() {
    try {
      const response = await fetch(baseURL + currentStopId);
      const data = await response.json();
      infoBox.textContent = `Next stop ${data.name}`;
      nextStop = data.name;
      currentStopId = data.next;
      departButton.disabled = true;
      arriveButton.disabled = false;
    } catch (error) {
      infoBox.textContent = "Error";
      departButton.disabled = true;
      arriveButton.disabled = true;
    }
  }

  function arrive() {
    infoBox.textContent = `Arriving at ${nextStop}`;
    departButton.disabled = false;
    arriveButton.disabled = true;
  }

  return {
    depart,
    arrive,
  };
}

let result = solve();
