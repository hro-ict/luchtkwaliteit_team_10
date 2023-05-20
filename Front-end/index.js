
const display = document.getElementById("display");
const testbtn = document.querySelector("#test");

testbtn.addEventListener("click", () => loadSavedModel() && console.log("Loading saved model.."));
