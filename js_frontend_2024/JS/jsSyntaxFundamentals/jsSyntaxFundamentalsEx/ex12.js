function cookingByNumbers(startingNumber, ...operations) {
    let result = parseInt(startingNumber);
    const myList = operations;
    
    operations.forEach(operation => {
        if (operation === "chop") {
            result /= 2;
            console.log(result);
        } else if (operation === "dice") {
            result = Math.sqrt(result);
            console.log(result);
        } else if (operation === "spice") {
            result += 1;
            console.log(result);
        } else if (operation === "bake") {
            result *= 3;
            console.log(result);
        } else if (operation === "fillet") {
            result -= 0.2 * result;
            console.log(result);
        }
    });
}

// cookingByNumbers('32', 'chop', 'chop', 'chop', 'chop', 'chop');
cookingByNumbers('9', 'dice', 'spice', 'chop', 'bake', 'fillet')