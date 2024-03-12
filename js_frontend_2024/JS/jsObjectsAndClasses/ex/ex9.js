function dictionaryMaker(jsonArrray) {
  const combinedObjects = {};
  jsonArrray.forEach((jsonString) => {
    const obj = JSON.parse(jsonString);

    Object.entries(obj).forEach(([term, description]) => {
      if (combinedObjects.hasOwnProperty(term)) {
        combinedObjects[term] = description;
      } else {
        combinedObjects[term] = description;
      }
    });
  });
  const sortedTerms = Object.keys(combinedObjects).sort();

  sortedTerms.forEach((term) => {
    console.log(`Term: ${term} => Definition: ${combinedObjects[term]}`);
  });
}

dictionaryMaker([
  '{"Coffee":"A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."}',
  '{"Bus":"A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare."}',
  '{"Boiler":"A fuel-burning apparatus or container for heating water."}',
  '{"Tape":"A narrow strip of material, typically used to hold or fasten something."}',
  '{"Microphone":"An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded."}',
]);
