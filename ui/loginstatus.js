const logout = document.getElementById('logout');
logout.style.cursor = 'pointer';

async function checkLogin() {
    let loggedIn = await eel.getLoginStatus()();
    if(!loggedIn) {
        document.getElementById('main').innerHTML = '<h1>Please login again</h1>';
    }
}

logout.addEventListener('click', async (e) => {
    await eel.logout();
    window.location.href = '../login.html';
});

if (logout !== null){
    checkLogin();
}
