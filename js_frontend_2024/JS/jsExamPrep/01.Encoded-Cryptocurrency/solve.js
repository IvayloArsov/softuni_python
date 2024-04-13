function solve(input) {
  let message = input.shift();

  for (let i = 0; i < input.length; i++) {
    const line = input[i];
    if (line === "Buy") {
      break;
    }
    if (line === "TakeEven") {
      let newMessage = "";
      for (j = 0; j < message.length; j += 2) {
        newMessage += message[j];
      }
      message = newMessage;
      console.log(message);
    } else if (line.startsWith("ChangeAll")) {
      const elements = line.split("?");
      const substring = elements[1];
      const replacement = elements[2];
      message = message.split(substring).join(replacement);
      console.log(message);
    } else if (line.startsWith("Reverse")) {
      const elements = line.split("?");
      const substring = elements[1];
      const index = message.indexOf(substring);
      if (index !== -1) {
        const reversed = substring.split("").reverse().join("");
        message =
          message.substring(0, index) +
          message.substring(index + substring.length) +
          reversed;
        console.log(message);
      } else {
        console.log("error");
      }
    }
  }
  console.log(`The cryptocurrency is: ${message}`);
}

// const inputCommands = [
//   "z2tdsfndoctsB6z7tjc8ojzdngzhtjsyVjek!snfzsafhscs",
//   "TakeEven",
//   "Reverse?!nzahc",
//   "ChangeAll?m?g",
//   "Reverse?adshk",
//   "ChangeAll?z?i",
//   "Buy",
// ];

// solve(inputCommands);

// const inputCommands = [
//   "PZDfA2PkAsakhnefZ7aZ",
//   "TakeEven",
//   "TakeEven",
//   "TakeEven",
//   "ChangeAll?Z?X",
//   "ChangeAll?A?R",
//   "Reverse?PRX",
//   "Buy",
// ];

// solve(inputCommands);
