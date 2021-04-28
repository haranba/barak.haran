// button with function that change attribute.
function click1() {
    document.body.innerHTML = document.body.innerHTML.replace("creative", "leader");
}

function click2() {
    document.body.innerHTML = document.body.innerHTML.replace("leader", "creative");
}

var ck_name = /^[A-Za-z0-9 ]{3,20}$/;
var ck_email = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;

function ValidateName(form) {
    var name = form.name.value;
    var errors = [];

    if (!ck_name.test(name)) {
        errors[errors.length] = "You valid Name .";
    }
    if (!ck_email.test(email)) {
        errors[errors.length] = "You must enter a valid email address.";
    }
    if (errors.length > 0) {

        reportErrors(errors);
        return false;
    }
    return true;
}

function reportErrors(errors) {
    var msg = "Please Enter Valide Data...\n";
    for (var i = 0; i < errors.length; i++) {
        var numError = i + 1;
        msg += "\n" + numError + ". " + errors[i];
    }
    alert(msg);
}
