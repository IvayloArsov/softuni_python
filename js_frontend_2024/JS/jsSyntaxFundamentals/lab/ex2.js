function printStudentInfo(name, age, averageGrade) {
  const formattedGrade = averageGrade.toFixed(2);
  console.log(`Name: ${name}, Age: ${age}, Grade: ${formattedGrade}`);
}

const studentName = "Asdf Fsda";
const studentAge = 20;
const studentAverageGrade = 123.456;

printStudentInfo(studentName, studentAge, studentAverageGrade);
