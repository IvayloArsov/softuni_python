function subtract() {
  console.log("TODO:...");
  const firstNumber = parseFloat(document.getElementById("firstNumber").value);
  const secondNumber = parseFloat(
    document.getElementById("secondNumber").value
  );
  const result = firstNumber - secondNumber;
  document.getElementById("result").innerText = result;
}
