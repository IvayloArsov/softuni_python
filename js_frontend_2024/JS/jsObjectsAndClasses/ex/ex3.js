function updateStock(currentStock, orderedProducts) {
  const stockObject = {};

  for (let i = 0; i < currentStock.length; i += 2) {
    const productName = currentStock[i];
    const quantity = Number(currentStock[i + 1]);
    stockObject[productName] = quantity;
  }
  for (let i = 0; i < orderedProducts.length; i += 2) {
    const productName = orderedProducts[i];
    const quantity = Number(orderedProducts[i + 1]);

    if (stockObject.hasOwnProperty(productName)) {
      stockObject[productName] += quantity;
    } else {
      stockObject[productName] = quantity;
    }
  }
  for (const [product, quantity] of Object.entries(stockObject)) {
    console.log(`${product} -> ${quantity}`);
  }
}

updateStock(
  ["Salt", "2", "Fanta", "4", "Apple", "14", "Water", "4", "Juice", "5"],
  ["Sugar", "44", "Oil", "12", "Apple", "7", "Tomatoes", "7", "Bananas", "30"]
);
