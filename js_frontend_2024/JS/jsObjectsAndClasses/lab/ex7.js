function solve(input) {
  let addressBook = {};
  for (let line of input) {
    let [name, address] = line.split(":");
    if (addressBook.hasOwnProperty(name)) {
      addressBook[name] = address;
    } else {
      addressBook[name] = address;
    }
  }
  let addressArray = Object.entries(addressBook);

  addressArray.sort((a, b) => {
    keyA = a[0];
    keyB = b[0];
    return keyA.localeCompare(keyB);
  });
  for (let [key, value] of addressArray) {
    console.log(`${key} -> ${value}`);
  }
}

solve([
  "Bob:Huxley Rd",
  "John:Milwaukee Crossing",
  "Peter:Fordem Ave",
  "Bob:Redwing Ave",
  "George:Mesta Crossing",
  "Ted:Gateway Way",
  "Bill:Gateway Way",
  "John:Grover Rd",
  "Peter:Huxley Rd",
  "Jeff:Gateway Way",
  "Jeff:Huxley Rd",
]);
