function solve(input) {
  const employees = parseInt(input.shift());
  const employeesList = {};
  for (let i = 0; i < employees; i++) {
    const [employeeName, shift, coffees] = input[i].split(" ");
    employeesList[employeeName] = {
      shift: shift,
      coffees: coffees.split(","),
    };
  }
  for (let i = employees; i < input.length; i++) {
    let line = input[i];
    if (line === "Closed") break;
    const parts = line.split(" / ");
    const command = parts[0];
    const employeeName = parts[1];

    if (command === "Prepare") {
      const orderShift = parts[2];
      const orderCoffee = parts[3];
      if (
        employeesList[employeeName].shift === orderShift &&
        employeesList[employeeName].coffees.includes(orderCoffee)
      ) {
        console.log(`${employeeName} has prepared a ${orderCoffee} for you!`);
      } else {
        console.log(
          `${employeeName} is not available to prepare a ${orderCoffee}.`
        );
      }
    }
    if (command === "Change Shift") {
      const newShift = parts[2];
      employeesList[employeeName].shift = newShift;
      console.log(`${employeeName} has updated his shift to: ${newShift}`);
    }
    if (command === "Learn") {
      const newCoffee = parts[2];
      if (employeesList[employeeName].coffees.includes(newCoffee)) {
        console.log(`${employeeName} knows how to make ${newCoffee}.`);
      } else {
        employeesList[employeeName].coffees.push(newCoffee);
        console.log(
          `${employeeName} has learned a new coffee type: ${newCoffee}.`
        );
      }
    }
  }
  Object.keys(employeesList).forEach((worker) => {
    console.log(
      `Barista: ${worker}, Shift: ${
        employeesList[worker].shift
      }, Drinks: ${employeesList[worker].coffees.join(", ")}`
    );
  });
}

let a = [
  "3",
  "Alice day Espresso,Cappuccino",
  "Bob night Latte,Mocha",
  "Carol day Americano,Mocha",
  "Prepare / Alice / day / Espresso",
  "Change Shift / Bob / night",
  "Learn / Carol / Latte",
  "Learn / Bob / Latte",
  "Prepare / Bob / night / Latte",
  "Closed",
];
solve(a);
