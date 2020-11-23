const noticeController = document.getElementById('notice');
const submit = document.getElementById('submit');
const noticesController = document.getElementById('notices');
const successMsgController = document.getElementById('success');

submit.addEventListener('click', async (e) => {
    successMsgController.innerText = '';

    let notice = noticeController.value;

    let success = await eel.updateNotice(notice)();

    console.log(success);

    successMsgController.innerText = success? 'Sucessfully Updated Notice': 'Error during updation';

    let notices = await eel.getNotices()();

    noticesController.innerText = '';

    for(n of notices) {
        noticesController.innerHTML += `${n[0]}<br>`;
    }
});

