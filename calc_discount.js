const prices = [99, 129, 149];
const discount = 0.1;

function applyDiscount(prices, discount) {
 for (let i = 0; i < prices.length; i++) {
  console.log(prices[i] * discount);
 }
}
applyDiscount(prices, discount);
