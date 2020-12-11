const nameController = document.getElementById('name');
const regnoController = document.getElementById('regno');
const dobController = document.getElementById('dob');
const semController = document.getElementById('sem');
const departmentController = document.getElementById('department');

const marksDetailController = document.getElementById('marks-details')
const marksController = document.getElementById('marks');
const semNumberController = document.getElementById('sem-number');
const examTypeController = document.getElementById('exam');
const submitBtnController = document.getElementById('submit');

const studentFormController = document.getElementById('student-form');

let data = {};

marksDetailController.style.display = 'none';

async function displayDetails() {
    studentFormController.style.display = 'none';

    let regno = await eel.getRegno()();
    data = await eel.viewDetails('Student', regno)();

    console.log(data);
    
    nameController.textContent += data['name'];
    regnoController.textContent += data['regno'];
    dobController.textContent += data['dob'];
    semController.textContent += data['sem'];
    departmentController.textContent += data['department'];
    
    studentFormController.style.display = 'block';
}

submitBtnController.addEventListener('click', async(e) => {

    marksController.innerHTML = '';

    let sem = semNumberController.value;
    let type = examTypeController.value;
    let regno = await eel.getRegno()();

    let marks_data = await eel.getAllMarks(regno, data['department'], sem, type)();
    let attendance_data = await eel.getAttendance(regno, data['department'], sem)();
    
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

displayDetails();