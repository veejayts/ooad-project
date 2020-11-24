const logout = document.getElementById('logout');
console.log(logout)

async function checkLogin() {
    let loggedIn = await eel.getLoginStatus()();
    console.log(loggedIn);
    if(!loggedIn) {
        document.getElementById('main').innerHTML = 'Please login again';
    }
}

logout.addEventListener('click', async (e) => {
    await eel.logout();
    window.location.href = '../login.html';
});

if (logout !== null){
    checkLogin();
}