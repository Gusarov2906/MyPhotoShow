var email = document.getElementById("email");

function sizeValidate() {
var size = document.getElementById("email");

    if (!size.checkValidity()) {

        size.setCustomValidity("ERROR!");
    } else {
        size.setCustomValidity("");

    } 
}