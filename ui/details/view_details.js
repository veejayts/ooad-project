const search = document.getElementById('view-details');
const searchidController = document.getElementById('search-id');
const detailsController = document.getElementById('details');
const radios = document.getElementsByName('detailType');
const errorController = document.getElementById('error');

search.addEventListener('click', async (e) => {
    e.preventDefault();
    detailsController.innerHTML = '';
    errorController.innerText = '';
    let regno = searchidController.value;
    let detailType;

    for (var i = 0, length = radios.length; i < length; i++) {
        if (radios[i].checked) {
            detailType = radios[i].value;
            break;
        }
    }

    let details = await eel.viewDetails(detailType, regno)();

    console.log(details);

    if (details !== false) {
        for(const key in details) {
            let br = document.createElement('br');
            let p = document.createElement('p');
            p.textContent = `${key}: ${details[key]}`;
            detailsController.appendChild(p);
            detailsController.appendChild(br);
        }
    } else {
        errorController.innerText = '';
        errorController.innerText = 'Error: User not found, check details and try again';
    }
});