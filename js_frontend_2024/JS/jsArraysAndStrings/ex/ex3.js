function sortNames(names) {
  const namesWithLowerCase = names.map((name) => ({
    original: name,
    lowercased: name.toLowerCase(),
  }));

  namesWithLowerCase.sort((a, b) => a.lowercased.localeCompare(b.lowercased));

  for (let i = 0; i < namesWithLowerCase.length; i++) {
    console.log(`${i + 1}.${namesWithLowerCase[i].original}`);
  }
}

sortNames(["John", "Bob", "Christina", "Ema"]);
sortNames(["Ab", "cd", "bc"]);
