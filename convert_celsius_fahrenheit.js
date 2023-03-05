const celsius = 5;
const fahrenheit = 41;
const celsiusToFahrenheit = (celsius * 9 / 5) + 32;
const fahrenheitToCelsius = (fahrenheit - 32) * 5 / 9;
console.log("Temperature conversions");
console.log("-----------------------");
console.log(fahrenheit + " degrees Fahrenheit are:");
console.log(fahrenheitToCelsius + " degrees Celsius");
console.log("----");
console.log(celsius + " degrees celsius are:");
console.log(celsiusToFahrenheit + " degrees fahrenheit");
// with array
const fahrenheit = [72, 68, 70, 74, 77, 75, 79];
const celsius = [];
for (const element of fahrenheit) {
 let c = (element - 32) * (5/9);
 celsius.push(c);
}
console.log(celsius);
