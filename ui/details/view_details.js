const search = document.getElementById('view-details');
const searchidController = document.getElementById('search-id');
const detailsController = document.getElementById('details');
const radios = document.getElementsByName('detailType');
const errorController = document.getElementById('error');
const radioButtonsController = document.getElementById('radio-buttons');
const searchIdTextController = document.getElementById('search-id-text');
let loginType = '';

const detailsTitle = ['Name', 'Register Number', 'DOB', 'Attendance Percentage', 'Maths marks', 'English marks', 'Computer marks', 'Total marks percentage']

search.addEventListener('click', async (e) => {
    e.preventDefault();
    detailsController.innerHTML = '';
    errorController.innerText = '';
    let regno = searchidController.value;
    let detailType;

    if (loginType === 'Staff') {
        detailType = 'Student';
    } else {
        for (var i = 0, length = radios.length; i < length; i++) {
            if (radios[i].checked) {
                detailType = radios[i].value;
                break;
            }
        }
    }

    let details = await eel.viewDetails(detailType, regno)();

    console.log(details);

    if (details !== false) {
        let keys = Object.keys(details);
        for(let i = 0; i < keys.length; i++) {
            let tr = document.createElement('tr');
            let td1 = document.createElement('td');
            let td2 = document.createElement('td');
            td2.textContent = `${detailsTitle[i]}`;
            td1.textContent = `${details[keys[i]]}`;
            tr.appendChild(td2);
            tr.appendChild(td1);
            detailsController.appendChild(tr);
        }
    } else {
        errorController.innerText = '';
        errorController.innerText = 'Error: User not found, check details and try again';
        errorController.style.color = 'red';
    }
});

async function setBackPath() {
    loginType = await eel.getLoginType()();

    if (loginType === 'Staff') {
        document.getElementById('back').href = '../staff/dashboard.html';
        radioButtonsController.style.display = 'none';
    } else {
        searchIdTextController.innerText = 'Enter register no. of student or ID of staff'
        document.getElementById('back').href = '../admin/dashboard.html';
    }
}

setBackPath();