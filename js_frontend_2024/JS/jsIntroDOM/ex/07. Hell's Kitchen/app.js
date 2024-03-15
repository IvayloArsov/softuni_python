function solve() {
  document.querySelector("#btnSend").addEventListener("click", onClick);

  function onClick() {
    const inputTextArea = document.querySelector("textarea").value;
    const inputArray = JSON.parse(inputTextArea);
    const restaurantsObj = {};

    inputArray.forEach((restaurant) => {
      const [restaurantName, workersInfo] = restaurant.split(" - ");
      const workers = workersInfo.split(", ");
      let totalSalary = 0;
      let maxSalary = 0;

      if (!restaurantsObj[restaurantName]) {
        restaurantsObj[restaurantName] = {
          avgSalary: 0,
          maxSalary: 0,
          workers: [],
        };
      }

      workers.forEach((worker) => {
        const [workerName, workerSalary] = worker.split(" ");
        const salary = parseInt(workerSalary);
        totalSalary += salary;
        maxSalary = Math.max(maxSalary, salary);

        restaurantsObj[restaurantName].workers.push({
          name: workerName,
          salary: salary,
        });
      });

      const avgSalary = totalSalary / workers.length;
      restaurantsObj[restaurantName].avgSalary = avgSalary.toFixed(2);
      restaurantsObj[restaurantName].maxSalary = maxSalary.toFixed(2);
    });

    let bestRestaurantName = "";
    let bestRestaurantAvgSalary = 0;
    let bestRestaurantMaxSalary = 0;

    for (const [name, data] of Object.entries(restaurantsObj)) {
      if (parseFloat(data.avgSalary) > bestRestaurantAvgSalary) {
        bestRestaurantName = name;
        bestRestaurantAvgSalary = parseFloat(data.avgSalary);
        bestRestaurantMaxSalary = parseFloat(data.maxSalary);
      }
    }

    const bestRestaurantOutput = document.querySelector("#bestRestaurant p");
    const bestWorkersOutput = document.querySelector("#workers p");

    bestRestaurantOutput.textContent = `Name: ${bestRestaurantName} Average Salary: ${bestRestaurantAvgSalary.toFixed(
      2
    )} Best Salary: ${bestRestaurantMaxSalary.toFixed(2)}`;

    const workers = restaurantsObj[bestRestaurantName].workers.sort(
      (a, b) => b.salary - a.salary
    );

    let workersString = "";
    workers.forEach((worker) => {
      workersString += `Name: ${worker.name} With Salary: ${worker.salary} `;
    });
    bestWorkersOutput.textContent = workersString;
  }
}
