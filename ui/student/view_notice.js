const noticesController = document.getElementById('notices');

async function getNotices() {
    let notices = await eel.getNotices()();

    noticesController.innerText = '';

    for(n of notices) {
        noticesController.innerHTML += `${n[0]}<br>`;
    }
}

getNotices();