const arr = [3, 5, 6, 8, 9, 11, 12, 14, 15];
const callback = (num) => num % 3 === 0;
let divisibleByThree = null;

function doMath() {
 divisibleByThree = arr.filter(callback);
 return divisibleByThree;
}
doMath();
console.log(divisibleByThree);
console.log("These numbers are divisible by 3");
