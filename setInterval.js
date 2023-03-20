let blinkerOn = false;
const toggleBlinker = () => {
 if (blinkerOn) {
  console.log("Blinker off");
  blinkerOn = false;
 } else {
  console.log("Blinker on");
  blinkerOn = true;
 }
};
setInterval(toggleBlinker, 500);
