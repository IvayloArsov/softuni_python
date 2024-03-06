function solve(firstName, lastName, age) {
  let personDict = {};
  personDict.firstName = firstName;
  personDict.lastName = lastName;
  personDict.age = age;
  return personDict;
}

console.log(solve("Peter", "Pan", "20"));
