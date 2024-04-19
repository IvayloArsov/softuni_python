document.addEventListener("DOMContentLoaded", () => {
  const baseUrl = "http://localhost:3030/jsonstore/games/";
  const gamesList = document.getElementById("games-list");
  const addButton = document.getElementById("add-game");
  const editButton = document.getElementById("edit-game");
  const gameNameInput = document.getElementById("g-name");
  const gameTypeInput = document.getElementById("type");
  const gamePlayersInput = document.getElementById("players");
  const loadButton = document.getElementById("load-games");

  loadButton.addEventListener("click", loadGames);
  addButton.addEventListener("click", addGame);
  editButton.addEventListener("click", editGame);

  let currentEditingId = null;

  function loadGames() {
    fetch(baseUrl)
      .then((response) => response.json())
      .then((data) => {
        gamesList.innerHTML = "";
        Object.keys(data).forEach((key) => {
          displayGame(data[key], key);
        });
      });
  }

  function displayGame(game) {
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
    changeBtn.addEventListener("click", () => setupEdit(game, game._id));
    const deleteBtn = div.querySelector(".delete-btn");
    deleteBtn.addEventListener("click", () => deleteGame(game._id));
    gamesList.appendChild(div);
  }

  function addGame() {
    const gameData = {
      name: gameNameInput.value,
      type: gameTypeInput.value,
      players: gamePlayersInput.value,
    };

    fetch(baseUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(gameData),
    }).then(() => {
      clearForm();
      loadGames();
    });
  }

  function clearForm() {
    gameNameInput.value = "";
    gameTypeInput.value = "";
    gamePlayersInput.value = "";
    editButton.disabled = true;
    addButton.disabled = false;
    currentEditingId = null;
  }

  function setupEdit(game, id) {
    gameNameInput.value = game.name;
    gameTypeInput.value = game.type;
    gamePlayersInput.value = game.players;
    editButton.disabled = false;
    addButton.disabled = true;
    currentEditingId = id;
  }

  function editGame() {
    const gameData = {
      name: gameNameInput.value,
      type: gameTypeInput.value,
      players: gamePlayersInput.value,
    };

    fetch(`${baseUrl + currentEditingId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(gameData),
    }).then(() => {
      clearForm();
      loadGames();
    });
  }

  function deleteGame(id) {
    fetch(`${baseUrl + id}`, {
      method: "DELETE",
    }).then(() => {
      loadGames();
    });
  }
});
