const fruits = ['apples', 'bananas', 'oranges'];

function searchFruits(fruits, searchPhrase) {
 const foundFruit = fruits.find(fruit => fruit === searchPhrase);
 if (foundFruit) {
  console.log(searchPhrase + ' are in the fruit basket!');
 }
 else {
  console.log('No such fruit in the fruit basket!');

 }
}

searchFruits(fruits, 'apples');
