function toggle() {
  const extra = document.getElementById("extra");
  const button = document.getElementsByClassName("button")[0];

  if (extra.style.display === "none" || extra.style.display === "") {
    extra.style.display = "block";
    button.textContent = "Less";
  } else {
    extra.style.display = "none";
    button.textContent = "More";
  }
}
