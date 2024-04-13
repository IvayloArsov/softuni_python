async function loadGames() {
  const response = await fetch(baseUrl);
  const data = await response.json();
  const gamesList = document.getElementById("games-list");
  gamesList.innerHTML = "";
  Object.keys(data).forEach((key) => displayGame(data[key], key));
}

function displayGame(game, id) {
  const gamesList = document.getElementById("games-list");
  const div = document.createElement("div");
  div.className = "board-game";
  div.innerHTML = `
      <div class="content">
        <p>${game.name}</p>
        <p>${game.type}</p>
        <p>${game.players}</p>
      </div>
      <div class="buttons-container">
        <button class="change-btn">Change</button>
        <button class="delete-btn">Delete</button>
      </div>
    `;
  const changeBtn = div.querySelector(".change-btn");
  changeBtn.addEventListener("click", () => setupEdit(game, id));
  const deleteBtn = div.querySelector(".delete-btn");
  deleteBtn.addEventListener("click", () => deleteGame(id));
  gamesList.appendChild(div);
}

async function editGame(id) {
  let gameNameInput = document.getElementById("g-name");
  let gameTypeInput = document.getElementById("type");
  let gamePlayersInput = document.getElementById("players");

  let gameData = {
    name: gameNameInput.value,
    type: gameTypeInput.value,
    players: gamePlayersInput.value,
  };

  await fetch(`${baseUrl}${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(gameData),
  });
  await loadGames();
  clearForm();
}

async function deleteGame(id) {
  await fetch(`${baseUrl}${id}`, {
    method: "DELETE",
  });
  await loadGames();
}
