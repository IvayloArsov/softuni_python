function solve(input) {
  const racers = parseInt(input.shift());
  const racingTeam = {};

  for (let i = 0; i < racers; i++) {
    const [riderName, fuelCapacity, position] = input[i].split("|");
    if (fuelCapacity > 100) {
      fuelCapacity = 100;
    }
    racingTeam[riderName] = {
      fuelCapacity: parseInt(fuelCapacity),
      position: parseInt(position),
    };
  }
  for (let i = racers; i < input.length; i++) {
    const line = input[i];
    if (line === "Finish") {
      break;
    }

    const parts = line.split(" - ");
    const command = parts[0];
    const name = parts[1];

    switch (command) {
      case "StopForFuel":
        const minimumFuel = parseInt(parts[2]);
        const newPosition = parseInt(parts[3]);
        if (racingTeam[name].fuelCapacity < minimumFuel) {
          racingTeam[name].position = newPosition;
          console.log(
            `${name} stopped to refuel but lost his position, now he is ${newPosition}.`
          );
        } else {
          console.log(`${name} does not need to stop for fuel!`);
        }
        break;

      case "Overtaking":
        const nameTwo = parts[2];
        if (racingTeam[name].position < racingTeam[nameTwo].position) {
          let temp = racingTeam[name].position;
          racingTeam[name].position = racingTeam[nameTwo].position;
          racingTeam[nameTwo].position = temp;
          console.log(`${name} overtook ${nameTwo}!`);
        }
        break;

      case "EngineFail":
        const lapsLeft = parseInt(parts[2]);
        console.log(
          `${name} is out of the race because of a technical issue, ${lapsLeft} laps before the finish.`
        );
        delete racingTeam[name];
      default:
        break;
    }
  }
  Object.keys(racingTeam).forEach((rider) => {
    console.log(`${rider}\n  Final position: ${racingTeam[rider].position}`);
  });
}

a = [
  "4",
  "Valentino Rossi|100|1",
  "Marc Marquez|90|3",
  "Jorge Lorenzo|80|4",
  "Johann Zarco|80|2",
  "StopForFuel - Johann Zarco - 90 - 5",
  "Overtaking - Marc Marquez - Jorge Lorenzo",
  "EngineFail - Marc Marquez - 10",
  "Finish",
];
solve(a);
