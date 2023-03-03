const numbers = [2, 3, 5, 7, 11];

function double(array) {
 const results = [];
 for (let i = 0; i < array.length; i++) {
  results.push(array[i] * array[i]);
 }
 console.log(results);
}

double(numbers);
