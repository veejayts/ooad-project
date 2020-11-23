const submit = document.getElementById("submit");
const radios = document.getElementsByName("detailType");
const studentRadio = document.getElementById("student");
const staffRadio = document.getElementById("staff");

const studentFormController = document.getElementById("student-form");
const staffFormController = document.getElementById("staff-form");

const name = document.getElementById('name');
const regno = document.getElementById('regno');
const dob = document.getElementById('dob');

const nameStaff = document.getElementById('name-staff');
const id = document.getElementById('id');

let loginType = 'Student';

studentRadio.addEventListener("click", (e) => {
    e.preventDefault();
    studentFormController.style.display = 'block';
    staffFormController.style.display = 'none';
    loginType = 'Student';
})

staffRadio.addEventListener("click", (e) => {
    e.preventDefault();
    staffFormController.style.display = 'block';
    studentFormController.style.display = 'none';
    loginType = 'Staff';
})

submit.addEventListener("click", async (e) => {
    e.preventDefault();
    console.log(loginType);
    let success;
    if(loginType === 'Staff') {
        console.log(nameStaff.value);
        console.log(id.value);
        success = await eel.enterDetails(loginType, id.value, nameStaff.value)();
    } else {
        console.log(regno.value);
        console.log(name.value);
        console.log(dob.value);
        success = await eel.enterDetails(loginType, regno.value, name.value, dob.value)();
    }
    console.log(success);
});