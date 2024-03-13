function search() {
  const towns = document.getElementById("towns");
  const searchText = document.getElementById("searchText").value.toLowerCase();
  const townElements = towns.getElementsByTagName("li");

  let matches = 0;

  for (let i = 0; i < townElements.length; i++) {
    townElements[i].innerHTML = townElements[i].textContent;
  }

  for (let i = 0; i < townElements.length; i++) {
    const townText = townElements[i].textContent.toLowerCase();
    if (townText.includes(searchText)) {
      townElements[i].style.fontWeight = "bold";
      townElements[i].style.textDecoration = "underline";
      matches++;
    }
  }
  const resultDiv = document.getElementById("result");
  resultDiv.textContent = `${matches} matches found`;
}
