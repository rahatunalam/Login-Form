document.querySelector("form").addEventListener(("submit"), function(e){
    const password = document.querySelector("input[name='password']").value;
    const confirmpassword = document.querySelector("input[name='confirm_password']").value;
    const error =  document.getElementById("error");

    if (confirmpassword != password){
        error.textContent="Passwords do not match!";
        e.preventDefault();
    }
});