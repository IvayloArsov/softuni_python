function parseJsonToObject(jsonString) {
  const parsedObject = JSON.parse(jsonString);
  for (const key in parsedObject) {
    console.log(`${key}: ${parsedObject[key]}`);
  }
}

parseJsonToObject('{"name": "George", "age": 40, "town": "Sofia"}');
parseJsonToObject('{"name": "Peter", "age": 35, "town": "Plovdiv"}');
