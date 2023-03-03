const newNumbers = [];

function multiply(arrayOne, arrayTwo) {
 let product;
 for (let i = 0; i < arrayOne.length; i++) {
  product = arrayOne[i] * arrayTwo[i];
  newNumbers.push(product);
 }
}

multiply([1,2,3,4], [5,6,7,8]);

console.log(newNumbers);
