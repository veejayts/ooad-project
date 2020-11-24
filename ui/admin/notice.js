const noticeController = document.getElementById('notice');
const submit = document.getElementById('submit');
const noticesController = document.getElementById('notices');
const successMsgController = document.getElementById('success');

submit.addEventListener('click', async (e) => {
    successMsgController.innerText = '';

    let notice = noticeController.value;

    let success = await eel.updateNotice(notice)();

    // console.log(success);

    if(success) {
        successMsgController.innerText = 'Sucessfully Updated Notice';
        successMsgController.style.color = 'green';
    } else {
        successMsgController.innerText = 'Error during updation';
        successMsgController.style.color = 'red';
    }

    getNotices();
});

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