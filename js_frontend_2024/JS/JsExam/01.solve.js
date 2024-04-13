function solve(input) {
  const gunslingers = parseInt(input[0], 10);
  const posse = {};

  for (let i = 1; i <= gunslingers; i++) {
    const [heroName, HP, bullets] = input[i].split(" ");
    posse[heroName] = {
      HP: parseInt(HP, 10),
      bullets: parseInt(bullets, 10),
    };
  }

  for (let i = gunslingers + 1; i < input.length; i++) {
    const command = input[i];
    if (command === "Ride Off Into Sunset") {
      break;
    }

    const parts = command.split(" - ");
    const action = parts[0];
    const characterName = parts[1];

    if (action === "FireShot") {
      const target = parts[2];
      if (posse[characterName].bullets > 0) {
        posse[characterName].bullets -= 1;
        console.log(
          `${characterName} has successfully hit ${target} and now has ${posse[characterName].bullets} bullets!`
        );
      } else {
        console.log(
          `${characterName} doesn't have enough bullets to shoot at ${target}!`
        );
      }
    } else if (action === "TakeHit") {
      const damage = parseInt(parts[2], 10);
      const attacker = parts[3];
      posse[characterName].HP -= damage;
      if (posse[characterName].HP > 0) {
        console.log(
          `${characterName} took a hit for ${damage} HP from ${attacker} and now has ${posse[characterName].HP} HP!`
        );
      } else {
        console.log(`${characterName} was gunned down by ${attacker}!`);
        delete posse[characterName];
      }
    } else if (action === "Reload") {
      const maxBullets = 6;
      if (posse[characterName].bullets < maxBullets) {
        const reloaded = maxBullets - posse[characterName].bullets;
        posse[characterName].bullets = maxBullets;
        console.log(`${characterName} reloaded ${reloaded} bullets!`);
      } else {
        console.log(`${characterName}'s pistol is fully loaded!`);
      }
    } else if (action === "PatchUp") {
      const amount = parseInt(parts[2], 10);
      if (posse[characterName].HP < 100) {
        const newHP = posse[characterName].HP + amount;
        const actualRecovered =
          newHP > 100 ? 100 - posse[characterName].HP : amount;
        posse[characterName].HP = Math.min(newHP, 100);
        console.log(
          `${characterName} patched up and recovered ${actualRecovered} HP!`
        );
      } else {
        console.log(`${characterName} is in full health!`);
      }
    }
  }

  Object.keys(posse).forEach((heroName) => {
    console.log(
      `${heroName}\n  HP: ${posse[heroName].HP}\n  Bullets: ${posse[heroName].bullets}`
    );
  });
}

const userInput = [
  "2",
  "Jesse 100 4",
  "Walt 100 5",
  "FireShot - Jesse - Bandit",
  "TakeHit - Walt - 30 - Bandit",
  "PatchUp - Walt - 20",
  "Reload - Jesse",
  "Ride Off Into Sunset",
];

solve(userInput);
