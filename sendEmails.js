import Axios from "axios"

function sendEmail(){
    var data = [
        { 
        "name" : document.getElementById("name").value,
        "mail": document.getElementById("mail").value,
        "phone-number": document.getElementById("phone-number").value,
        "message": document.getElementById("message").value
        }
    ];

    //TODO: Post request to axios to trigger sending the data
    return data;
}

var submit = document.getElementById('contact-submit');
submit.onclick = function(){
    sendEmail();
}