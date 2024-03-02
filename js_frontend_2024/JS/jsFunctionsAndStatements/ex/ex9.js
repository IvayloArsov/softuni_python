function loadingBar(progress) {
  const barLength = progress / 10;
  const loadingBar = `[${"%".repeat(barLength)}${".".repeat(10 - barLength)}]`;

  let result = [];

  if (progress < 100) {
    result.push(`${progress}% ${loadingBar}`);
    result.push("Still loading...");
  } else {
    result.push("100% Complete!");
    result.push(`${loadingBar}`);
  }
  console.log(result.join("\n"));
}

loadingBar(30);
loadingBar(100);
