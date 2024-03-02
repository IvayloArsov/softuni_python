function formatGrade(grade) {
  let gradeDescription;
  switch (true) {
    case grade < 3.0:
      gradeDescription = "Fail";
      grade = 2;
      break;
    case grade < 3.5:
      gradeDescription = "Poor";
      break;
    case grade < 4.5:
      gradeDescription = "Good";
      break;
    case grade < 5.5:
      gradeDescription = "Very good";
      break;
    default:
      gradeDescription = "Excellent";
  }
  const formattedGrade = grade < 3.0 ? grade : grade.toFixed(2);
  console.log(`${gradeDescription} (${formattedGrade})`);
}

formatGrade(2.99);
formatGrade(3.5);
