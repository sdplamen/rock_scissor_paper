const grades = [91, 66, 77, 84, 66];
const search = 66;

function searchGrade(grades, search) {
 for (let i = 0; i < grades.length; i++) {
  if (grades[i] === search) {
   console.log("The grade exists!");
   break;
  }
 }
}
searchGrade(grades, search);
