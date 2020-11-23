const nameController = document.getElementById('name');
const regnoController = document.getElementById('regno');
const dobController = document.getElementById('dob');
const attendanceController = document.getElementById('attendance');
const mathsController = document.getElementById('maths');
const englishController = document.getElementById('english');
const computerController = document.getElementById('computer');
const percentageController = document.getElementById('percentage');
const studentFormController = document.getElementById('student-form');

async function displayDetails() {
    studentFormController.style.display = 'none';

    let regno = await eel.getRegno()();
    let data = await eel.viewDetails('Student', regno)();

    console.log(data);
    
    nameController.textContent += data['name'];
    regnoController.textContent += data['regno'];
    dobController.textContent += data['dob'];
    attendanceController.textContent += data['attendance'];
    mathsController.textContent += data['maths_marks'];
    englishController.textContent += data['english_marks'];
    computerController.textContent += data['computer_marks'];
    percentageController.textContent += data['percentage_marks'];
    
    studentFormController.style.display = 'block';
}

displayDetails();