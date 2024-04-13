// document.addEventListener("DOMContentLoaded", () => {
//   const baseUrl = "http://localhost:3030/jsonstore/games/";
//   const gamesList = document.getElementById("games-list");
//   const addButton = document.getElementById("add-game");
//   const editButton = document.getElementById("edit-game");
//   const gameNameInput = document.getElementById("g-name");
//   const gameTypeInput = document.getElementById("type");
//   const gamePlayersInput = document.getElementById("players");
//   const loadButton = document.getElementById("load-games");

//   loadButton.addEventListener("click", loadGames);
//   addButton.addEventListener("click", addGame);
//   editButton.addEventListener("click", () => editGame(currentEditingId));

//   let currentEditingId = "";

//   function loadGames() {
//     fetch(baseUrl)
//       .then((response) => response.json())
//       .then((data) => {
//         gamesList.innerHTML = "";
//         for (const key of Object.keys(data)) {
//           displayGame(data[key], key);
//         }
//       });
//   }

//   function displayGame(game, id) {
//     const div = document.createElement("div");
//     div.className = "board-game";
//     div.innerHTML = `
//         <div class="content">
//           <p>${game.name}</p>
//           <p>${game.players}</p>
//           <p>${game.type}</p>
//         </div>
//         <div class="buttons-container">
//           <button class="change-btn">Change</button>
//           <button class="delete-btn">Delete</button>
//         </div>
//       `;
//     const changeBtn = div.querySelector(".change-btn");
//     changeBtn.addEventListener("click", () => setupEdit(game, id));
//     const deleteBtn = div.querySelector(".delete-btn");
//     deleteBtn.addEventListener("click", () => deleteGame(id));
//     gamesList.appendChild(div);
//   }

//   function addGame() {
//     const gameData = {
//       name: gameNameInput.value,
//       type: gameTypeInput.value,
//       players: gamePlayersInput.value,
//     };

//     fetch(baseUrl, {
//       method: "POST",
//       headers: { "Content-Type": "application/json" },
//       body: JSON.stringify(gameData),
//     }).then(() => {
//       clearForm();
//       loadGames();
//     });
//   }

//   function clearForm() {
//     gameNameInput.value = "";
//     gameTypeInput.value = "";
//     gamePlayersInput.value = "";
//     editButton.disabled = true;
//     addButton.disabled = false;
//     currentEditingId = "";
//   }

//   function setupEdit(game, id) {
//     gameNameInput.value = game.name;
//     gameTypeInput.value = game.type;
//     gamePlayersInput.value = game.players;
//     editButton.disabled = false;
//     addButton.disabled = true;
//     currentEditingId = id;
//   }

//   function editGame(id) {
//     const gameData = {
//       name: gameNameInput.value,
//       type: gameTypeInput.value,
//       players: gamePlayersInput.value,
//     };

//     fetch(`${baseUrl + id}`, {
//       method: "PUT",
//       body: JSON.stringify(gameData),
//     })
//       .then((response) => response.json())
//       .then(() => {
//         loadGames();
//         clearForm();
//       });
//   }

//   function deleteGame(id) {
//     fetch(`${baseUrl + id}`, {
//       method: "DELETE",
//     }).then(() => {
//       loadGames();
//     });
//   }
// });

const baseUrl = "http://localhost:3030/jsonstore/games/";
let currentEditingId = "";

// Global async functions
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

async function addGame() {
  const gameNameInput = document.getElementById("g-name");
  const gameTypeInput = document.getElementById("type");
  const gamePlayersInput = document.getElementById("players");

  await fetch(baseUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      name: gameNameInput.value,
      type: gameTypeInput.value,
      players: gamePlayersInput.value,
    }),
  });
  clearForm();
  loadGames();
}

function setupEdit(game, id) {
  const gameNameInput = document.getElementById("g-name");
  const gameTypeInput = document.getElementById("type");
  const gamePlayersInput = document.getElementById("players");
  const editButton = document.getElementById("edit-game");
  const addButton = document.getElementById("add-game");

  gameNameInput.value = game.name;
  gameTypeInput.value = game.type;
  gamePlayersInput.value = game.players;
  editButton.disabled = false;
  addButton.disabled = true;
  currentEditingId = id;
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

  await fetch(`${baseUrl + id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(gameData),
  });
  await loadGames();
  clearForm();
}

async function deleteGame(id) {
  await fetch(`${baseUrl + id}`, {
    method: "DELETE",
  });
  await loadGames();
}

function clearForm() {
  const gameNameInput = document.getElementById("g-name");
  const gameTypeInput = document.getElementById("type");
  const gamePlayersInput = document.getElementById("players");
  const editButton = document.getElementById("edit-game");
  const addButton = document.getElementById("add-game");

  gameNameInput.value = "";
  gameTypeInput.value = "";
  gamePlayersInput.value = "";
  editButton.disabled = true;
  addButton.disabled = false;
  currentEditingId = "";
}

document.addEventListener("DOMContentLoaded", () => {
  const addButton = document.getElementById("add-game");
  const editButton = document.getElementById("edit-game");
  const loadButton = document.getElementById("load-games");

  loadButton.addEventListener("click", loadGames);
  addButton.addEventListener("click", addGame);
  editButton.addEventListener("click", () => editGame(currentEditingId));
});
