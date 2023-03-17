let counter = 1;

function addPost() {
  const input = document.getElementById("inputPost").value;
  if (input != "") {
    counter++;
    document.getElementById("count").innerHTML = counter;
    const postDiv = document.createElement('div');
    postDiv.className = "post";
    document.getElementById("body").appendChild(postDiv);
    const p = document.createElement("p");
    p.innerHTML = input;
    postDiv.appendChild(p);
    const likeButton = document.createElement("button");
    p.innerHTML = "Like";
    postDiv.appendChild(likeButton);
    const commentButton = document.createElement("button");
    p.innerHTML = "Comment";
    postDiv.appendChild(commentButton);
    document.getElementById("inputPost").value = "";
  }
}
function remove() {
  let notificationDiv = document.getElementById("notification");
  document.getElementById("body").removeChild(notificationDiv);
}
