function convertObjToJson(name, lastName, hairColor) {
  const person = {
    name: name,
    lastName: lastName,
    hairColor: hairColor,
  };
  const jsonString = JSON.stringify(person);
  console.log(jsonString);
}

convertObjToJson("George", "Jones", "Brown");
