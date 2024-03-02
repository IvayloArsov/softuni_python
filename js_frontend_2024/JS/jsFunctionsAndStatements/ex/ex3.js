function printCharactersBetween(char1, char2) {
  const char1Code = char1.charCodeAt(0);
  const char2Code = char2.charCodeAt(0);

  const startCode = Math.min(char1Code, char2Code);
  const endCode = Math.max(char1Code, char2Code);

  for (let i = startCode + 1; i < endCode; i++) {
    const char = String.fromCharCode(i);
    process.stdout.write(char + " ");
  }

  process.stdout.write("\n");
}
printCharactersBetween("#", ":");
printCharactersBetween("C", "#");
