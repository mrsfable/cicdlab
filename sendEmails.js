function sendEmail(){
    var data =
        { 
        "name" : document.getElementById("name").value,
        "mail": document.getElementById("mail").value,
        "phone-number": document.getElementById("phone-number").value,
        "message": document.getElementById("message").value
        };
    console.log(data);
    //TODO: Post request to axios to trigger sending the data
    
   axios.post('http://localhost:5000/contact', data)
  .then(function (response) {
      console.log("SUCCESS");
      alert("Mail sent!");
  })
  .catch(function (error) {
      alert("Error, mail not sent!");
  });
  

    
    return data;
}

$(document).ready(function() {
    document.getElementById("contact-form").addEventListener("submit", function(e){
    e.preventDefault();
    sendEmail();
   });
});