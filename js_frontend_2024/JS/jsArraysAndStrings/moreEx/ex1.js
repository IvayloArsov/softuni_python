function login(arr) {
  const username = arr[0];
  const correctPassword = arr[0].split("").reverse().join("");
  let incorrectAttempts = 0;

  for (let i = 1; i <= 4; i++) {
    if (arr[i] === correctPassword) {
      console.log(`User ${username} logged in.`);
      return;
    } else {
      if (i < 4) {
        console.log(`Incorrect password. Try again.`);
        incorrectAttempts++;
      } else {
        console.log(`User ${username} blocked!`);
        return;
      }
    }
  }
}

login(["sunny", "rainy", "cloudy", "sunny", "not sunny"]);
login(["momo", "omom"]);
login(["Acer", "login", "go", "let me in", "recA"]);
