const input = document.querySelector("input");

function qtyChanged() {
  document.querySelector("p").innerHTML = "Total Price: $" + (Number(input.value) * 1.99);
}
input.onchange = qtyChanged;
