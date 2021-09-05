
var submitButton = document.getElementById("submit");

function chick1(){
  var error2 = document.getElementById("error2");
  var email = document.getElementById("email").value;
  var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

    if(email == ""){
        error2.innerHTML = "this field can't be empty";
        error2.style.color = "#F00";
        return false;
    }



  if(!email.match(mailformat)){
    error2.innerHTML = "enter a valid email";
    error2.style.color = "#f00";
    return false;
  }
  
 
  else{
    error2.innerHTML = "";
    return true;
  }
  
}



function chick2(){
  var error1 = document.getElementById("error1");
  var full_name = document.getElementById("full_name").value;
  if(full_name == ""){
    error1.innerHTML = "this field can't be empty";
    error1.style.color = "#F00";
    return false;
  }

  if(full_name != ""){
    error1.innerHTML = "";
    return true;
  }
  
}





function test(){
  // do whatever you like here
  chick1();
  chick2();
  
  if (chick1() && chick2()){
    submitButton.disabled = false;
  }else{
    submitButton.disabled = true;
  }
  setTimeout(test, 100);
};


