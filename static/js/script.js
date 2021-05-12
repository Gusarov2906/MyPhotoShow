var email = document.getElementById("email");

function sizeValidate() {
var size = document.getElementById("email");

    if (!size.checkValidity()) {

        size.setCustomValidity("ERROR!");
    } else {
        size.setCustomValidity("");

    } 
}

function checkNameSurname() {
    var name = document.getElementById("name");
    var surname = document.getElementById("surname");
    if (name.value.match("^[A-ZА-Я]{1}[a-zа-я]{1,10}$") )
    {
        name.setCustomValidity("");
    } else {
        name.setCustomValidity("Name must have only one uppercase symbol and not special symbols and numbers");
    }
    if (surname.value.match("^[A-ZА-Я]{1}[a-zа-я]{1,10}$") )
    {
        surname.setCustomValidity("");
    } else {
        surname.setCustomValidity("Surname must have only one uppercase symbol and not special symbols and numbers");
    }
}

function checkData() {
    var password = document.getElementById('password');
    var password_again = document.getElementById("password_again");

    if (password.value != password_again.value || password.value == "") {
        password_again.setCustomValidity("Passwords don't match");
        password.setCustomValidity("Passwords don't match");
    } else {
        password_again.setCustomValidity("");
        password.setCustomValidity("");
    }
}

function  check()
{
    checkNameSurname();
    checkData();
}
