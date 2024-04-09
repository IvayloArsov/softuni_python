function attachEvents() {
  const baseUrl = "http://localhost:3030/jsonstore/messenger";
  const refreshButtonElement = document.querySelector("#refresh");
  const textAreaElement = document.querySelector("#messages");
  refreshButtonElement.addEventListener("click", retrieveTextMessages);
  const sendButtonElement = document.querySelector("#submit");
  sendButtonElement.addEventListener("click", sendTextMessage);
  async function retrieveTextMessages() {
    fetch(baseUrl)
      .then((response) => response.json())
      .then((msgs) => {
        const messages = Object.values(msgs)
          .map((msg) => `${msg.author}: ${msg.content}`)
          .join("\n");
        textAreaElement.value = messages;
      });
  }
  async function sendTextMessage() {
    const authorInput = document.querySelector("[name='author']");
    const contentInput = document.querySelector("[name='content']");
    const newMessage = {
      author: authorInput.value,
      content: contentInput.value,
    };
    authorInput.value = "";
    contentInput.value = "";
    fetch(baseUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newMessage),
    })
      .then((response) => response.json())
      .then((data) => {
        refreshMessages();
        authorInput.value = "";
        contentInput.value = "";
      });
  }
}

attachEvents();
