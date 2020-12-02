const searchBtn = document.getElementById('search');
const submitBtn = document.getElementById('submit');
const searchController = document.getElementById('search-field');
const studentFormController = document.getElementById('student-form');
const errorController = document.getElementById('error');
const attendanceErrorController = document.getElementById('attendance-error');

const nameController = document.getElementById('name');
const regnoController = document.getElementById('regno');
const dobController = document.getElementById('dob');
const attendanceController = document.getElementById('attendance');
const mathsController = document.getElementById('maths');
const englishController = document.getElementById('english');
const computerController = document.getElementById('computer');
const percentageController = document.getElementById('percentage');

errorController.style.color = 'red';
attendanceErrorController.style.color = 'red';

mathsController.addEventListener('change', (e) => {
    percentageController.value = ((Number(mathsController.value) + Number(englishController.value) + Number(computerController.value)) / 300) * 100;
});

englishController.addEventListener('change', (e) => {
    percentageController.value = ((Number(mathsController.value) + Number(englishController.value) + Number(computerController.value)) / 300) * 100;
});

computerController.addEventListener('change', (e) => {
    percentageController.value = ((Number(mathsController.value) + Number(englishController.value) + Number(computerController.value)) / 300) * 100;
});

searchBtn.addEventListener('click', async (e) => {
    errorController.innerText = '';
    attendanceErrorController.innerText = '';
    studentFormController.style.display = 'none';

    let regno = searchController.value;
    let data = await eel.viewDetails('Student', regno)();

    if (data === false) {
        errorController.innerText = 'Error. Check details and try again.'
        return;
    }

    console.log(data);
    
    nameController.value = data['name'];
    regnoController.value = data['regno'];
    dobController.value = data['dob'];
    attendanceController.value = data['attendance'];
    mathsController.value = data['maths_marks'];
    englishController.value = data['english_marks'];
    computerController.value = data['computer_marks'];
    percentageController.value = ((Number(mathsController.value) + Number(englishController.value) + Number(computerController.value)) / 300) * 100;
    
    studentFormController.style.display = 'block';
});

submitBtn.addEventListener('click', async (e) => {
    attendanceErrorController.innerText = '';

    let name = nameController.value;
    let regno = regnoController.value;
    let dob = dobController.value;
    let attendance = attendanceController.value;
    let maths = mathsController.value;
    let english = englishController.value;
    let computer = computerController.value;
    let percentage = percentageController.value;

    // console.log(name);
    // console.log(regno)
    // console.log(dob)
    // console.log(attendance)
    // console.log(maths)
    // console.log(english)
    // console.log(computer)
    // console.log(percentage)

    let success = false;
    let aboveLimit = true;
    let attendanceAboveLimit = true;

    if (attendance <= 100) {
        attendanceAboveLimit = false;
    }

    if (((Number(mathsController.value) + Number(englishController.value) + Number(computerController.value)) / 300) * 100 <= 100) {
        aboveLimit = false;
    }
    
    if (!aboveLimit && !attendanceAboveLimit) {
        success = eel.updateDetails(name, regno, dob, attendance, maths, english, computer, percentage)();
    }

    if(success) {
        errorController.innerText = 'Successfully updated details';
        errorController.style.color = 'green';
    } else {
        errorController.innerText = 'Error, could not update details';
        aboveLimit? errorController.innerText = 'Error, could not update details. Total marks percentage above 100' : 'Error, could not update details.';
        attendanceAboveLimit? attendanceErrorController.innerText = 'Error, attendance percentage cannot be above 100': '';
    }
});

async function setBackPath() {
    const loginType = await eel.getLoginType()();
    if (loginType === 'Staff') {
        document.getElementById('back').href = '../staff/dashboard.html'
    } else {
        document.getElementById('back').href = '../admin/dashboard.html'
    }
}

setBackPath();