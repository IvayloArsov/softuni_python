function createObjectsFromTable(inputArray) {
  const objectsArray = [];

  for (const row of inputArray) {
    const [town, latitudeStr, longitudeStr] = row.split(" | ");
    const latitude = parseFloat(latitudeStr).toFixed(2);
    const longitude = parseFloat(longitudeStr).toFixed(2);

    const resultObject = {
      town: town,
      latitude: latitude,
      longitude: longitude,
    };

    objectsArray.push(resultObject);
  }

  objectsArray.forEach((element) => {
    console.log(element);
  });
}

createObjectsFromTable(["Plovdiv | 136.45 | 812.575"]);
