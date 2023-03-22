const arr = [1, 2, 3, 4, 5];
const tripleTheNum = (num) => num * 3;
let newArray = null;
function doMath() {
 newArray = arr.map(tripleTheNum);
 return newArray;
}
doMath();
console.log(newArray);
console.log("The values in the array have been tripled");
