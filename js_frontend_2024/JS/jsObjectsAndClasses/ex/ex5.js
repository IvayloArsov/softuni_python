function manageInventory(heroesArr) {
  const heroes = heroesArr.map((heroInfo) => {
    const [Hero, level, items] = heroInfo.split(" / ");
    return {
      Hero,
      level: parseInt(level),
      items: items ? items.split(", ") : [],
    };
  });

  heroes.sort((a, b) => a.level - b.level);

  for (const { Hero, level, items } of heroes) {
    console.log(
      `Hero: ${Hero}\nlevel => ${level}\nitems => ${items.join(", ")}`
    );
  }
}

manageInventory([
  "Batman / 2 / Banana, Gun",
  "Superman / 18 / Sword",
  "Poppy / 28 / Sentinel, Antara",
]);

// function manageInventory(heroesArr) {
//   const heroes = [];

//   for (const heroInfo of heroesArr) {
//     const splitHeroInfo = heroInfo.split(" / ");
//     const heroName = splitHeroInfo[0];
//     const heroLevel = parseInt(splitHeroInfo[1]);
//     const heroInventory = splitHeroInfo[2] ? splitHeroInfo[2].split(", ") : [];

//     const heroObject = {
//       Hero: heroName,
//       level: heroLevel,
//       items: heroInventory,
//     };
//     heroes.push(heroObject);
//   }
//   heroes.sort((a, b) => a.level - b.level);

//   for (const hero of heroes) {
//     console.log(`Hero: ${hero.Hero}`);
//     console.log(`level => ${hero.level}`);
//     console.log(`items => ${hero.items.join(", ")}`);
//   }
// }
