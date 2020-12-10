const submit = document.getElementById("submit");
const radios = document.getElementsByName("detailType");
const studentRadio = document.getElementById("student");
const staffRadio = document.getElementById("staff");

const studentFormController = document.getElementById("student-form");
const staffFormController = document.getElementById("staff-form");

const name = document.getElementById('name');
const regno = document.getElementById('regno');
const dob = document.getElementById('dob');
const studentDepartment = document.getElementById('student-department');
const sem = document.getElementById('sem');

const nameStaff = document.getElementById('name-staff');
const id = document.getElementById('id');
const staffDepartment = document.getElementById('staff-department');

const successMsgController = document.getElementById('success-msg');

let loginType = 'Student';
studentRadio.style.backgroundColor = 'aqua';

studentRadio.addEventListener("click", (e) => {
    e.preventDefault();
    successMsgController.innerText = '';
    studentFormController.style.display = 'block';
    staffFormController.style.display = 'none';
    studentRadio.style.backgroundColor = 'aqua';
    staffRadio.style.backgroundColor = '';
    loginType = 'Student';
})

staffRadio.addEventListener("click", (e) => {
    e.preventDefault();
    successMsgController.innerText = '';
    staffFormController.style.display = 'block';
    studentFormController.style.display = 'none';
    studentRadio.style.backgroundColor = '';
    staffRadio.style.backgroundColor = 'aqua';
    loginType = 'Staff';
})

submit.addEventListener("click", async (e) => {
    e.preventDefault();
    console.log(loginType);
    let success;
    if(loginType === 'Staff') {
        console.log(nameStaff.value);
        console.log(id.value);
        console.log(staffDepartment.value)
        success = await eel.enterDetails(loginType, id.value, nameStaff.value, '', staffDepartment.value)();
    } else {
        console.log(regno.value);
        console.log(name.value);
        console.log(dob.value);
        success = await eel.enterDetails(loginType, regno.value, name.value, dob.value, studentDepartment.value, sem.value)();
    }
    console.log(success);

    if (success) {
        successMsgController.innerText = 'Successfully Inserted';
        successMsgController.style.color = 'green';
    } else {
        successMsgController.innerText = 'Error inserting into database';
        successMsgController.style.color = 'red';
    }
});