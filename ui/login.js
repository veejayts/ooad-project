const regnoController = document.getElementById("regno");
const passwordController = document.getElementById("password");
const submit = document.getElementById("login");
const radios = document.getElementsByName("loginType");

submit.addEventListener("click", async (e) => {
    e.preventDefault();
    let regno = regnoController.value;
    let password = passwordController.value;
    let loginType;

    for (var i = 0, length = radios.length; i < length; i++) {
        if (radios[i].checked) {
            loginType = radios[i].value;
            break;
        }
    }

    let isValid = await eel.login(regno, password, loginType)();

    console.log(isValid);
    console.log(loginType)

    if (isValid) {
        if (loginType === "Admin"){
            window.location.href = "./admin/dashboard.html";}
        else if (loginType === "Staff"){
            window.location.href = "./staff/dashboard.html";}
        else if (loginType === "Student"){
            window.location.href = "./student/dashboard.html";
        }
    } else {
        let error = document.getElementById("error");
        error.innerHTML = "";
        let h2 = document.createElement("h2");
        h2.innerText = "Invalid regno or password. Try again.";
        error.appendChild(h2);
    }
});
