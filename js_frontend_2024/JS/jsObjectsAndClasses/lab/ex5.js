function phoneBook(input) {
  let phonebook = {};
  for (let line of input) {
    let tokens = line.split(" ");
    let name = tokens[0];
    let number = tokens[1];
    phonebook[name] = number;
  }
  for (let key in phonebook) {
    console.log(`${key} -> ${phonebook[key]}`);
  }
}

phoneBook(["George 0552554", "Peter 087587", "George 0453112", "Bill 0845344"]);
