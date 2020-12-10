const subCodeController = document.getElementById('subcode');
const semNumberController = document.getElementById('sem-number');
const updateSectionController = document.getElementById('update-section');
const studentController = document.getElementById('student');
const updateBtnController = document.getElementById('update-btn');
const submitBtnController = document.getElementById('submit');
const errorController = document.getElementById('error');
const examTypeController = document.getElementById('exam');
const successController = document.getElementById('success');

errorController.style.color = 'red';
updateSectionController.style.display = 'none';

async function setBackPath() {
    const loginType = await eel.getLoginType()();
    if (loginType === 'Staff') {
        document.getElementById('back').href = '../staff/dashboard.html';
    } else {
        document.getElementById('back').href = '../admin/dashboard.html';
    }
}

updateBtnController.addEventListener('click', async(e) => {
    studentController.innerHTML = '';
    errorController.innerText = '';

    let subcode = subCodeController.value;
    let sem = semNumberController.value;
    
    let subcodes = await eel.getSubjectCodes(sem)();
    console.log(subcode);
    console.log(subcodes);

    if(subcodes.includes(subcode)) {
        updateSectionController.style.display = 'block';
        let regnos = await eel.getSubjectAttendance(sem, subcode)();
        console.log(regnos)

        for(let i of regnos) {
            let tr = document.createElement('tr');
            let td1 = document.createElement('td');
            let td2 = document.createElement('td');

            td1.innerText = i[0];
            td2.innerHTML = `
                <div class="input-field">
                    <input id="${i[0]}" type="number" class="validate" value=${i[1]}>
                    <label for="subcode">Attendance</label>
                </div>`;
            tr.appendChild(td1)
            tr.appendChild(td2)
            studentController.appendChild(tr);
        }

    } else {
        errorController.innerText = 'Wrong subject code';
    }
});

submitBtnController.addEventListener('click', async (e) => {
    successController.innerText = '';

    let sem = semNumberController.value;
    let regnos = await eel.getSubjectAttendance(sem, subCodeController.value)();
    let data = [];

    console.log(regnos);

    for(let i of regnos) {
        let temp = document.getElementById(i[0]);
        data.push([i[0], temp.value]);
    }

    let success = await eel.setAttendance(sem, data, subCodeController.value)();

    if(success) {
        successController.innerText = 'Success inserting';
        successController.style.color = 'green';
    } else {
        successController.innerText = 'Error, recheck the values';
        successController.style.color = 'red';
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, []);
});

setBackPath();