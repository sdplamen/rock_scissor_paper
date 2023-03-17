const item = document.querySelector("div");
const el = document.querySelectorAll("button");

function changeWidth() {
 item.classList.toggle("width");
}

function changeHeight() {
 item.classList.toggle("height");
}
el[0].addEventListener("click", changeHeight);
el[0].addEventListener("click", changeWidth);
el[1].addEventListener("click", changeHeight);
el[2].addEventListener("click", changeWidth);
