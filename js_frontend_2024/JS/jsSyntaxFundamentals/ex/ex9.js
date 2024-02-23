function fruits(fruit, grams, cost) {
    let price = (grams/1000)*cost;
    console.log(`I need \$${(price.toFixed(2))} to buy ${(grams/1000).toFixed(2)} kilograms ${fruit}.`);
}

fruits('orange', 2500, 1.80)
fruits('apple', 1563, 2.35)