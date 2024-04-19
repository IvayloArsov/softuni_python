function solve(input) {
  let spell = input.shift();

  for (let i = 0; i < input.length; i++) {
    const line = input[i];
    if (line === "End") {
      break;
    }
    const parts = line.split("!");
    const command = parts[0];

    if (command === "RemoveEven") {
      let newSpell = "";
      for (let j = 0; j < spell.length; j += 2) {
        newSpell += spell[j];
      }
      spell = newSpell;
      console.log(spell);
    } else if (command === "TakePart") {
      const fromIndex = parseInt(parts[1]);
      const toIndex = parseInt(parts[2]);
      spell = spell.slice(fromIndex, toIndex);
      console.log(spell);
    } else if (command === "Reverse") {
      const substring = parts[1];
      const index = spell.indexOf(substring);
      if (index !== -1) {
        const before = spell.substring(0, index);
        const after = spell.substring(index + substring.length);
        const reversed = substring.split("").reverse().join("");
        spell = before + after + reversed;
        console.log(spell);
      } else {
        console.log("Error");
      }
    }
  }

  console.log(`The concealed spell is: ${spell}`);
}

// const sampleInput = [
//   "asAsl2adkda2mdaczsa",
//   "RemoveEven",
//   "TakePart!1!9",
//   "Reverse!maz",
//   "End",
// ];

// solve(sampleInput);
