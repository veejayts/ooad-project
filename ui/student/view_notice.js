const noticesController = document.getElementById('notices');

async function getNotices() {
    let notices = await eel.getNotices()();

    noticesController.innerHTML = '';

    if(notices.length === 0) {
        noticesController.innerHTML = '<tr><td>No Notices</td></tr>';
    } else {
        for(n of notices) {
            noticesController.innerHTML += `<tr><td>${n[0]}</td></tr>`;
        }
    }
}

getNotices();