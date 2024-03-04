const BaseURL = "https://oumaru.com/api/";
var services;

services = axios.get(`${BaseURL}services/`).then((response) => {
    services = response.data.results;


    //Get blocs of services
    // let servicesRow = document.querySelector('#services-row');
    // let servicesBlock = servicesRow.cloneNode(true)
    // servicesBlock = servicesBlock.querySelector('#services-block');
    let servicesRow = document.querySelector("#services-block");

    for (i = 0; i < services.length; i++) {
        let servicesRow = document.querySelector("#services-block");
        let servicesBlock = servicesRow.cloneNode(true);
        servicesBlock = servicesBlock.querySelector("#service");
        servicesBlock.id = `service-${i}`;
        // console.log(servicesBlock.querySelector('#price-1'))
        servicesBlock.querySelector("#title-1").id = `title-${i}`;
        servicesBlock.querySelector(`#title-${i}`).textContent = services[i].name;

        //UPDATE pirce id
        servicesBlock.querySelector("#price-1").id = `price-${i}`;

        //format price
        const price = services[i].price;
        const fcfa = new Intl.NumberFormat("de-DE", {
            currency: "XOF",
            style: "currency",
        }).format(price);
        servicesBlock.querySelector(`#price-${i}`).textContent = services[i].delay;

        //get img and update id
        servicesBlock.querySelector("#img-1").id = `img-${i}`;
        servicesBlock.querySelector(`#img-${i}`).src = "https://res.cloudinary.com/dfunbusnr/" + services[i].image;

        //change input checkbox id
        servicesBlock.querySelector("#checkbox").id = `checkbox-${services[i].id}`;

        //append element on the block
        servicesRow.appendChild(servicesBlock);
    }
    document.querySelector("#service").remove();
    // document.querySelector('#checkbox').remove();
});

//get sevices checked
let checkboxs = document.getElementsByName("services");
var servicesSelected = [];

setInterval(() => {
    servicesSelected = [];
    let checkboxs = document.getElementsByName("services");
    for (i = 0; i < checkboxs.length; i++) {
        // console.log(checkboxs[i].checked);
        if (checkboxs[i].checked == true) {
            //get element html id end take a last char and convert to int for getting of service id
            let elementId;
            elementId = checkboxs[i].id;
            elementId = parseInt(elementId[elementId.length - 1]);
            servicesSelected.push(elementId);
        }
    }
    let toast = document.getElementById("toast");
    if(validateServices()){
        toast.classList.remove('animate__animated', 'animate__fadeOut');
        toast.classList.add("displayNoneToast", 'bg-warning');
        toast.textContent = 'Votre demande de devis a été prise en compte, veuillez verifier votre mail !';
        toast.classList.remove('bg-danger');
    }
    // console.log(servicesSelected);
}, 500);


function isDigit(str) {
    return /^\d+$/.test(str);
}
function checkEmail(email) {
    var expr = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
    return expr.test(email);
}

//Validations functions

//Function for validate last name
function validateLastName(){
    let lastName = document.getElementById("last_name").value;

    if(lastName === ''){
        document.getElementById("lastNameError").style.display = "block";
        return false;
    }else{
        document.getElementById("lastNameError").style.display = "none";
        return true;
    }
}
let lastNameInput = document.getElementById("last_name");
lastNameInput.addEventListener('input', validateLastName);


// function for validate first name
function validateFirstName(){
    let firstName = document.getElementById("first_name").value;

    if(firstName === ''){
        document.getElementById("firstNameError").style.display = "block";
        return false;
    }else{
        document.getElementById("firstNameError").style.display = "none";
        return true;
    }
}
let firstNameInput = document.getElementById("first_name");
firstNameInput.addEventListener('input', validateFirstName);


// function for validation email
function validateEmail(){
    let email = document.getElementById("email").value;

    if (email === "" || !checkEmail(email)) {
        document.getElementById("emailError").style.display = "block";
        return false;
    } else {
        document.getElementById("emailError").style.display = "none";
        return true;
    }
}
let emailInput = document.getElementById("email");
emailInput.addEventListener('input', validateEmail);


// function for contact validation
function validateContact(){
    let contact = document.getElementById("contact").value;

    if (contact === "" || !isDigit(contact) || contact.length < 8) {
        document.getElementById("contactError").style.display = "block";
        return false;
    } else {
        document.getElementById("contactError").style.display = "none";
        return true;
    }
}
let contactInput = document.getElementById("contact");
contactInput.addEventListener('input', validateContact);


// function for address validations
function validateAddress(){
    let address = document.getElementById("address").value;

    if (address === "") {
        document.getElementById("addressError").style.display = "block";
        return false;
    } else {
        document.getElementById("addressError").style.display = "none";
        return true;
    }
}
let addressInput = document.getElementById("address");
addressInput.addEventListener('input', validateAddress);

// function for budget validation
function validateBudget(){
    let budget = document.getElementById("budget").value;

    if (budget === "" || !isDigit(budget)) {
        document.getElementById("budgetError").style.display = "block";
        return false;
    } else {
        document.getElementById("budgetError").style.display = "none";
        return true;
    }
}
let budgetInput = document.getElementById("budget");
budgetInput.addEventListener('input', validateBudget);


// function for project description validations
function validateProjectDescription(){
    let projectDescription = document.getElementById("project_description").value;

    if (projectDescription === "") {
        document.getElementById("projectDescriptionError").style.display = "block";
        return false;
    } else {
        document.getElementById("projectDescriptionError").style.display = "none";
        return true;
    }
}
let projectDescriptionTextarea = document.getElementById("project_description");
projectDescriptionTextarea.addEventListener('input', validateProjectDescription);



//function for validate delay
function validateDelay(){
    let delay = document.getElementById("delay").value;

    if (delay === "") {
        document.getElementById("delayError").style.display = "block";
        return false;
    } else {
        document.getElementById("delayError").style.display = "none";
        return true;
    }
}
let delayInput = document.getElementById("delay");
delayInput.addEventListener('input', validateDelay);


function validateServices(){
    if(servicesSelected.length < 1){
        return false;
    }else{
        return true;
    }
}

// function validator() {

//     if (!lastNameValid || !firstNameValid || !emailValid || !contactValid || !addressValid || !budgetValid || !delayValid) {
//         return true;
//     }
//     return false;
// }

let estimator = document.querySelector("#estimator");
let estimator2 = estimator;
estimator.addEventListener("click", (e) => {
    e.preventDefault();
    let lastNameValid = validateLastName();
    let firstNameValid = validateFirstName();
    let emailValid = validateEmail();
    let contactValid = validateContact();
    let addressValid = validateAddress();
    let budgetValid = validateBudget();
    let delayValid = validateDelay();
    let servicesValid = validateServices();


    if (!lastNameValid || !firstNameValid || !emailValid || !contactValid || !addressValid || !budgetValid || !delayValid || !servicesValid) {
        document.getElementById("scrollTop").click();

        let toast = document.getElementById("toast");
        if(!servicesValid){
            //display
            toast.classList.remove('animate__animated', 'animate__fadeOut');
            toast.classList.remove("displayNoneToast", 'bg-warning');
            toast.textContent = 'Vous devez sélectionner au moins un service !';
            toast.classList.add('bg-danger');
        }else{
            toast.classList.remove('animate__animated', 'animate__fadeOut');
            toast.classList.add("displayNoneToast", 'bg-warning');
            toast.textContent = 'Votre demande de devis a été prise en compte, veuillez verifier votre mail !';
            toast.classList.remove('bg-danger');
        }
    }else {
        estimator.disabled = true;
        estimator.classList.add("px-5", "py-1");

        // disbaled all inputs
        let inputs = document.querySelectorAll("input");
        for (i = 0; i < inputs.length; i++) {
            inputs[i].disabled = true;
        }

        //disbaled textarea
        document.getElementById("project_description").disabled = true;

        // disbaled all checkbox
        for (i = 0; i < checkboxs.length; i++) {
            checkboxs[i].disabled = true;
        }
        //insert loader
        estimator.innerHTML = '<div class="spinner-border" role="status"><span class="sr-only">Loading...</span></div>';

        // Group all the elements
        let lastName = document.getElementById("last_name").value;
        let firstName = document.getElementById("first_name").value;
        let email = document.getElementById("email").value;
        let contact = document.getElementById("contact").value;
        let companyName = document.getElementById("company_name").value;
        let address = document.getElementById("address").value;
        let budget = document.getElementById("budget").value;
        let delay = document.getElementById("delay").value;
        let projectDescription = document.getElementById("project_description").value;

        const data = {
            last_name: lastName,
            first_name: firstName,
            email: email,
            contact: contact,
            company_name: companyName,
            address: address,
            budget: budget,
            delay: delay,
            project_description: projectDescription,
            services: servicesSelected,
        };

        axios.post("https://oumaru.com/api/send-devis-mail", data).then((response) => {
            //manage toastification
            let toast = document.getElementById("toast");
            //display
            toast.classList.remove("displayNoneToast");

            setTimeout(() => {
                toast.classList.add('animate__animated', 'animate__fadeOut');
            }, 3500);

            // enable all inputs
            let inputs = document.querySelectorAll("input");
            for (i = 0; i < inputs.length; i++) {
                inputs[i].disabled = false;
            }

            //enable textarea
            document.getElementById("project_description").disabled = false;

            // enable all checkbox
            for (i = 0; i < checkboxs.length; i++) {
                checkboxs[i].checked = false;
            }
            //delete loader
            estimator.innerHTML = "";
            estimator.classList.remove("px-5", "py-1");
            estimator.textContent = "Soumettre";
            estimator.disabled = false;
            lastName = document.getElementById("last_name").value = "";
            firstName = document.getElementById("first_name").value = "";
            email = document.getElementById("email").value = "";
            contact = document.getElementById("contact").value = "";
            company_name = document.getElementById("company_name").value = "";
            address = document.getElementById("address").value = "";
            budget = document.getElementById("budget").value = "";
            delay = document.getElementById("delay").value = "";
            projectDescription = document.getElementById("project_description").value = "";

            setTimeout(() => {
                toast.classList.add("displayNoneToast");
            }, 4300);
        }).catch((error)=>{
            alert(error);
        });
    }
});
