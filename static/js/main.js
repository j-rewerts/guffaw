function reqListener () {
  console.log(this.responseText);
}

var button = document.getElementById("button");

button.addEventListener("click", function() {
  console.log("Button clicked");

  var oReq = new XMLHttpRequest();
  oReq.addEventListener("load", reqListener);
  oReq.open("GET", "http://localhost:5000");
  oReq.send();
});
