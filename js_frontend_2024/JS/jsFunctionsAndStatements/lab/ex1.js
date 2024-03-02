function formatGrade(grade) {
  let gradeDescription;
  switch (true) {
    case grade < 3.0:
      gradeDescription = "Fail";
      break;
    case grade < 3.5:
      gradeDescription = "Poor";
      break;
    case grade < 4.5:
      gradeDescription = "Good";
      break;
    case grade < 5.5:
      gradeDescription = "Very Good";
      break;
    default:
      gradeDescription = "Excellent";
  }
  console.log(`Grade: ${grade.toFixed(2)} - ${gradeDescription}`);
}

formatGrade(3.33);
