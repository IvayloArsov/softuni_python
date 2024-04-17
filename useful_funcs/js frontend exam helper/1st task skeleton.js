function solve(input) {

// change var names
  const astronauts = parseInt(input.shift());
  const explorationTeam = {};

// for loop for filling up the object with the info, change var names
  for (let i = 0; i < astronauts; i++) {
    const [astronautName, oxygenLevel, energyReserve] = input[i].split(" ");
    explorationTeam[astronautName] = {
      oxygenLevel: parseInt(oxygenLevel),
      energyReserve: parseInt(energyReserve),
    };
  }
  
  // starting the loop over commands
  for (let i = astronauts; i < input.length; i++) {
    const line = input[i];
// change the breakpoint
    if (line === "End") {
      break;
    }
    
    //check split format
    const parts = line.split(" - ");
    //check if any of these variables must be made into Number format
    const command = parts[0];
    const name = parts[1];
    const amount = parseInt(parts[2]);
//this part below is different on each given task, might have to redo the whole thing
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
  
  //the print section - change accordingly to the format, but it should work
  Object.keys(explorationTeam).forEach((astronaut) => {
    console.log(
      `Astronaut: ${astronaut}, Oxygen: ${explorationTeam[astronaut].oxygenLevel}, Energy: ${explorationTeam[astronaut].energyReserve}`
    );
  });
}
