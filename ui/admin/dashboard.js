const optionsController = document.getElementById('options');
const pageTitleController = document.getElementById('page-title');
const options = ['View Details', 'enter staff details', 'enter student details']

const enterDetailsBtn = document.getElementById('enter-details');

async function updateTitle() {
    const loginType = await eel.getLoginType()();
    pageTitleController.innerText = `${loginType} Dashboard`;
}

updateTitle();