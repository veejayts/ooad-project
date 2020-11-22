const regnoController = document.getElementById("regno")
const passwordController = document.getElementById("password")
const submit = document.getElementById("login")

submit.addEventListener('click', async (e) => {
    let regno = regnoController.value;
    let password = passwordController.value;
    let isValid = await eel.login(regno, password, 'admin')();
    console.log(isValid);
});