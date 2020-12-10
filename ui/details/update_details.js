const searchBtn = document.getElementById('search');
const submitBtn = document.getElementById('submit');
const searchController = document.getElementById('search-field');
const studentFormController = document.getElementById('student-form');
const errorController = document.getElementById('error');

const nameController = document.getElementById('name');
const regnoController = document.getElementById('regno');
const dobController = document.getElementById('dob');
const departmentController = document.getElementById('department');
const semController = document.getElementById('sem');

errorController.style.color = 'red';

searchBtn.addEventListener('click', async (e) => {
    errorController.innerText = '';
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
    departmentController.value = data['department'];
    semController.value = data['sem'];

    studentFormController.style.display = 'block';
});

submitBtn.addEventListener('click', async (e) => {
    let name = nameController.value;
    let regno = regnoController.value;
    let dob = dobController.value;
    let department = departmentController.value;
    let sem = semController.value;

    let success = false;
    let aboveLimit = true;
    
    success = eel.updateDetails(name, regno, dob, department, sem)();

    if(success) {
        errorController.innerText = 'Successfully updated details';
        errorController.style.color = 'green';
    } else {
        errorController.innerText = 'Error, could not update details';
        aboveLimit? errorController.innerText = 'Error, could not update details. Total marks percentage above 100' : 'Error, could not update details.';
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