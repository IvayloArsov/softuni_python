async function lockedProfile() {
  const baseUrl = "http://localhost:3030/jsonstore/advanced/profiles";
  const main = document.getElementById("main");
  main.innerHTML = "";
  fetch(baseUrl)
    .then((response) => response.json())
    .then((data) => {
      Object.entries(data).forEach(([id, userInfo], index) => {
        const profile = document.createElement("div");
        profile.classList.add("profile");
        profile.innerHTML = `
            <img src="./iconProfile2.png" class="userIcon" />
            <label>Lock</label>
            <input type="radio" name="user${
              index + 1
            }Locked" value="lock" checked>
            <label>Unlock</label>
            <input type="radio" name="user${
              index + 1
            }Locked" value="unlock"><br>
            <hr>
            <label>Username</label>
            <input type="text" name="user${index + 1}Username" value="${
          userInfo.username
        }" disabled readonly />
            <div id="user${index + 1}HiddenFields" style="display: none;">
                <hr>
                <label>Email:</label>
                <input type="email" name="user${index + 1}Email" value="${
          userInfo.email
        }" disabled readonly />
                <label>Age:</label>
                <input type="text" name="user${index + 1}Age" value="${
          userInfo.age
        }" disabled readonly />
            </div>
            <button onclick="toggleShowMore(this, 'user${
              index + 1
            }Locked')">Show more</button>`;
        main.appendChild(profile);
      });
    });
  window.toggleShowMore = function (button, lockName) {
    const profile = button.parentNode;
    const lockStatus = profile.querySelector(
      `input[name="${lockName}"][value="lock"]`
    ).checked;
    const hiddenFieldsDiv = profile.querySelector('div[id^="user"]');
    if (!lockStatus) {
      if (button.textContent === "Show more") {
        hiddenFieldsDiv.style.display = "block";
        button.textContent = "Hide it";
      } else {
        hiddenFieldsDiv.style.display = "none";
        button.textContent = "Show more";
      }
    }
  };
}
