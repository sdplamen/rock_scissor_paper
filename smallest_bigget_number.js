function difference(array)
let biggest = array[0];
  let smallest = array[0];
  for (let i = 0; i < array.length; i++) {
    if (array[i] > biggest) {
      biggest = array[i];
    }
    if (array[i] < smallest) {
      smallest = array[i];
    }
  }
  return biggest - smallest;
}
