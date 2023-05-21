
//HTML
const display = document.getElementById("display");
const testbtn = document.querySelector("#test");

testbtn.addEventListener("click", () => loadSavedModel() && console.log("Loading saved model.."));

//moet nog wat in de fetch
function loadSavedModel() {
    fetch("...")
        .then((response) => response.json())
        .then((model) => modelLoaded(model))
}

if (luchtkwaliteit == 1) {
    display.innerText = `luchtkwaliteti is goed`
} else {
    display.innerText = `luchtkwaliteit is slecht`
}
