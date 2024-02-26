function distanceValidity(x1, y1, x2, y2) {
  function calculateDistance(x1, y1, x2, y2) {
    return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
  }

  function isInteger(value) {
    return Number.isInteger(value);
  }

  function checkDistanceValidity(x1, y1, x2, y2) {
    const distance1 = calculateDistance(x1, y1, 0, 0);
    const distance2 = calculateDistance(x2, y2, 0, 0);
    const distance3 = calculateDistance(x1, y1, x2, y2);

    if (isInteger(distance1)) {
      console.log(`{${x1}, ${y1}} to {0, 0} is valid`);
    } else {
      console.log(`{${x1}, ${y1}} to {0, 0} is invalid`);
    }

    if (isInteger(distance2)) {
      console.log(`{${x2}, ${y2}} to {0, 0} is valid`);
    } else {
      console.log(`{${x2}, ${y2}} to {0, 0} is invalid`);
    }

    if (isInteger(distance3)) {
      console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`);
    } else {
      console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`);
    }
  }

  checkDistanceValidity(x1, y1, x2, y2);
}

distanceValidity(2, 1, 1, 1);
distanceValidity(3, 0, 0, 4);
