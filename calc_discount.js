// first manner
const prices = [99, 129, 149];
const discount = 0.1;
function applyDiscount(prices, discount) {
 for (let i = 0; i < prices.length; i++) {
  console.log(prices[i] * discount);
 }
}
applyDiscount(prices, discount);
// second manner
const receipt = [5.99, 6.79, 3.89, 9.99, 2.50];
const applyDiscount = (total) => total * 0.9;
const total = (pricesArray) => {
  let sum = 0;
  for (let i = 0; i < pricesArray.length; i++) {
    sum += pricesArray[i];
  }
  return sum;
};
const subtotal = total(receipt);
console.log("Subtotal: " + subtotal.toFixed(2));
const discountedTotal = applyDiscount(subtotal);
console.log("Discounted Total: " + discountedTotal.toFixed(2));
