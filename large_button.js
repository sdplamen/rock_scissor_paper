const element = document.querySelector("button");

function login() {
 log.innerText = "User logged in.";
}

function makeBig() {
 element.style.fontSize = "2em";
}
element.onclick = makeBig;
