function solution() {
  const baseUrl = "http://localhost:3030/jsonstore/advanced/articles/";
  let main = document.getElementById("main");
  main.innerHTML = "";

  async function loadArticles() {
    const res = await fetch(`${baseUrl}list`);
    const data = await res.json();
    data.forEach((article) => {
      const divAccordion = document.createElement("div");
      divAccordion.className = "accordion";

      divAccordion.innerHTML = `
            <div class="head">
              <span>${article.title}</span>
              <button class="button" id="${article._id}">More</button>
            </div>
            <div class="extra" style="display: none;"><p></p></div>`;

      main.appendChild(divAccordion);

      const button = divAccordion.querySelector(".button");
      button.addEventListener("click", () => toggleContent(button));
    });
  }

  async function toggleContent(button) {
    const contentDiv = button.parentNode.nextElementSibling;
    const isMore = button.textContent === "More";
    if (isMore) {
      const res = await fetch(`${baseUrl}details/${button.id}`);
      const data = await res.json();
      contentDiv.querySelector("p").textContent = data.content;
      contentDiv.style.display = "block";
      button.textContent = "Less";
    } else {
      contentDiv.style.display = "none";
      button.textContent = "More";
    }
  }

  loadArticles();
}

solution();
