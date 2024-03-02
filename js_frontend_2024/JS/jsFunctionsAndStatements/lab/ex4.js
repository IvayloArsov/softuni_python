function calcOrders(item, quantity) {
  const itemsDict = {
    coffee: 1.5,
    water: 1.0,
    coke: 1.4,
    snacks: 2.0,
  };
  let result = itemsDict[item] * quantity;
  console.log(result.toFixed(2));
}

calcOrders("water", 5);
calcOrders("coffee", 2);
