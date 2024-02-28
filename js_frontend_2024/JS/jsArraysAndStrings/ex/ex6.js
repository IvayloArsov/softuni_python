function findHashTags(inputString) {
  const arr = inputString.split(" ");
  const result = [];

  arr.forEach((str) => {
    if (str.startsWith("#") && str.length > 1) {
      const specialWord = str.substring(1);
      if (/^[a-zA-Z]+$/.test(specialWord)) {
        result.push(specialWord);
      }
    }
  });

  return result.join("\n");
}

const a = findHashTags(
  "Nowadays everyone uses # to tag a #special word in #socialMedia"
);

console.log(a);
console.log("-".repeat(10));

const b = findHashTags(
  "The symbol # is known #variously in English-speaking #regions as the #number sign"
);

console.log(b);
