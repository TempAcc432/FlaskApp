let results = document.getElementsByClassName("row result")

// For each result in our table it will add an onclick function to each dropdownBtn
for (i = 0; i < results.length; i++){
    let dropdownBtn = results[i].querySelector('#dropdown-btn');
    let fontDropdown = results[i].querySelector('#font-dropdown');
    let result = results[i] // why I have to do this before entering the function bewilders me

   dropdownBtn.onclick = function () {
        if (result.style.height == '30px') {
            result.style.height = '200px';
            fontDropdown.className = "fa-solid fa-sort-down";
        }
        else {
            result.style.height = '30px';
            fontDropdown.className = "fa-sharp fa-solid fa-sort-up";
        }
    }
}

// Reveal text boxes when user checks checkbox
// good explanation: https://stackoverflow.com/questions/25870898/input-field-appear-after-selecting-a-check-box-html
function revealBox(cbox) {
    if (cbox.checked) {
      var inputBox = document.createElement("input");
      inputBox.type = "text";
      inputBox.name = cbox.value;
      inputBox.id = cbox.value;
      var div = document.createElement("div");
      div.id = cbox.name;
      div.innerHTML = cbox.value + ": ";
      div.appendChild(inputBox);
      document.getElementById("user-input").appendChild(div);
    } else {
      document.getElementById(cbox.name).remove();
    }
  }


// Map
map = document.getElementById("test")
viewBox = document.getElementById("map-viewbox")
var scale = 1,
panning = false,
pointX = 0,
pointY = 0,
start = {x : 0, y : 0}

function set_transform(){
    map.style.transform = "translate("+ pointX + "px," + pointY + "px) scale("+ scale + ")";
}

map.onmousedown = function(event) {
    event.preventDefault();
    start = {x: event.clientX - pointX, y: event.clientY - pointY};
    panning = true;

}

map.onmouseup = function(event) {
    panning = false;
}

map.onmousemove = function(event) {
    event.preventDefault();
    
    if (!panning){
        return;
    }
    pointX = (event.clientX - start.x);
    pointY = (event.clientY - start.y);
    set_transform();
}

map.onwheel = function(event) {
    event.preventDefault();
        set_transform();
}
