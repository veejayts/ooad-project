const search = document.getElementById('view-details');
const searchidController = document.getElementById('search-id');
const detailsController = document.getElementById('details');
const radios = document.getElementsByName('detailType');
const errorController = document.getElementById('error');
const radioButtonsController = document.getElementById('radio-buttons');
const searchIdTextController = document.getElementById('search-id-text');

const moreDetailsController = document.getElementById('more');

const marksDetailController = document.getElementById('marks-details')
const marksController = document.getElementById('marks');
const semNumberController = document.getElementById('sem-number');
const examTypeController = document.getElementById('exam');
const submitBtnController = document.getElementById('submit');

let details = {};
let loginType = '';

const detailsTitle = ['Register Number', 'Name', 'DOB', 'Department', 'Sem']

marksDetailController.style.display = 'none';
moreDetailsController.style.display = 'none';

search.addEventListener('click', async (e) => {
    e.preventDefault();
    detailsController.innerHTML = '';
    marksDetailController.style.display = 'none';
    moreDetailsController.style.display = 'none';
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

    details = await eel.viewDetails(detailType, regno)();

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
        if(detailType === 'Student') {
            moreDetailsController.style.display = 'block';
        }
    } else {
        errorController.innerText = '';
        errorController.innerText = 'Error: User not found, check details and try again';
        errorController.style.color = 'red';
    }
});

submitBtnController.addEventListener('click', async(e) => {
    marksController.innerHTML = '';

    let sem = semNumberController.value;
    let type = examTypeController.value;

    let marks_data = await eel.getAllMarks(searchidController.value, details['department'], sem, type)();
    let attendance_data = await eel.getAttendance(searchidController.value, sem)();
    
    if(marks_data !== []) {
        marksDetailController.style.display = 'block';
        
        for(let i = 0; i < marks_data.length; i++) {
            let tr = document.createElement('tr');
            let td1 = document.createElement('td');
            let td2 = document.createElement('td');
            let td3 = document.createElement('td');

            td1.textContent = marks_data[i][0];
            td2.textContent = marks_data[i][1];
            td3.textContent = attendance_data[i][1];

            tr.appendChild(td1);
            tr.appendChild(td2);
            tr.appendChild(td3);

            marksController.appendChild(tr);
        }
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, []);
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