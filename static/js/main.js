function reqListener () {
  console.log(this.responseText);
  var name = JSON.parse(this.responseText);
  joke.innerHTML=name[0].text;
}

var button = document.getElementById("button");

var joke = document.getElementById("joke");

button.addEventListener("click", function() {
  console.log("Button clicked");

  var oReq = new XMLHttpRequest();
  oReq.addEventListener("load", reqListener);
  oReq.open("GET", "http://localhost:5000/joke/random");
  oReq.send();
});
