function listEmployees(input) {
  const employeeDict = {};

  input.forEach((name) => {
    const personalNumber = name.length;
    employeeDict[name] = personalNumber;
  });
  for (const [name, personalNum] of Object.entries(employeeDict)) {
    console.log(`Name: ${name} -- Personal Number: ${personalNum}`);
  }
}

listEmployees(["Samuel Jackson", "Will Smith", "Bruce Willis", "Tom Holland"]);
