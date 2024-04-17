function solve(input) {
  const astronauts = parseInt(input.shift());
  const explorationTeam = {};

  for (let i = 0; i < astronauts; i++) {
    const [astronautName, oxygenLevel, energyReserve] = input[i].split(" ");
    explorationTeam[astronautName] = {
      oxygenLevel: parseInt(oxygenLevel),
      energyReserve: parseInt(energyReserve),
    };
  }
  for (let i = astronauts; i < input.length; i++) {
    const line = input[i];

    if (line === "End") {
      break;
    }
    const parts = line.split(" - ");
    const command = parts[0];
    const name = parts[1];
    const amount = parseInt(parts[2]);

    if (command === "Explore") {
      if (explorationTeam[name].energyReserve >= amount) {
        explorationTeam[name].energyReserve -= amount;
        console.log(
          `${name} has successfully explored a new area and now has ${explorationTeam[name].energyReserve} energy!`
        );
      } else {
        console.log(`${name} does not have enough energy to explore!`);
      }
    } else if (command === "Refuel") {
      const previousEnergy = explorationTeam[name].energyReserve;
      explorationTeam[name].energyReserve += amount;

      if (explorationTeam[name].energyReserve > 200) {
        explorationTeam[name].energyReserve = 200;
      }
      const difference = explorationTeam[name].energyReserve - previousEnergy;
      console.log(`${name} refueled their energy by ${difference}!`);
    } else if (command === "Breathe") {
      const previousOxygen = explorationTeam[name].oxygenLevel;
      explorationTeam[name].oxygenLevel += amount;

      if (explorationTeam[name].oxygenLevel > 100) {
        explorationTeam[name].oxygenLevel = 100;
      }
      const diff = explorationTeam[name].oxygenLevel - previousOxygen;
      console.log(`${name} took a breath and recovered ${diff} oxygen!`);
    }
  }
  Object.keys(explorationTeam).forEach((astronaut) => {
    console.log(
      `Astronaut: ${astronaut}, Oxygen: ${explorationTeam[astronaut].oxygenLevel}, Energy: ${explorationTeam[astronaut].energyReserve}`
    );
  });
}
// let a = [
//   "4",
//   "Alice 60 100",
//   "Bob 40 80",
//   "Charlie 70 150",
//   "Dave 80 180",
//   "Explore - Bob - 60",
//   "Refuel - Alice - 30",
//   "Breathe - Charlie - 50",
//   "Refuel - Dave - 40",
//   "Explore - Bob - 40",
//   "Breathe - Charlie - 30",
//   "Explore - Alice - 40",
//   "End",
// ];

// solve(a);
