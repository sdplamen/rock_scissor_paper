let counter = 3;
function upvote() {
  counter ++;
  document.getElementById("votes").innerText = counter + " Votes";
}
function downvote() {
  counter --;
  document.getElementById("votes").innerText = counter + " Votes";
}
