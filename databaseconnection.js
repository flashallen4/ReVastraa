const firebaseConfig = {
    apiKey: "AIzaSyBBKbhruCsA8Vz_tmV056aDsfWKzlTBjIg",
    authDomain: "revastra-215a9.firebaseapp.com",
    databaseURL: "https://revastra-215a9-default-rtdb.firebaseio.com",
    projectId: "revastra-215a9",
    storageBucket: "revastra-215a9.appspot.com",
    messagingSenderId: "208937722721",
    appId: "1:208937722721:web:6c165ad37ee2a87f5cdb20"
};

//initialize firebase
firebase.initializeApp(firebaseConfig);

// reference your database
var userDetailsDB = firebase.database().ref('userDetails');
var mailsSubscriptionDB = firebase.database().ref('MonthlySubscription');

document.getElementById('signup_details').addEventListener('submit', submitForm)
document.getElementById('mails_subscription').addEventListener('submit', agree_to_monthly_newsletter)

function submitForm(e){
    e.preventDefault();

    var F_name = getElementVal('inputF_Name');
    var L_name = getElementVal('inputL_Name');
    var emailid = getElementVal('inputEmail4');
    var password = getElementVal('inputPassword4');
    var state = getElementVal('inputState');

    saveMessages(F_name, L_name, emailid, password, state)
    
    //reset the form
    document.getElementById('signup_details').reset();
}

function agree_to_monthly_newsletter(e){
    e.preventDefault();

    var newsletter = getElementVal('newsletter1');

    added_to_mailinglist(newsletter)

    //reset the form
    document.getElementById('mails_subscription').reset();
}

const saveMessages = (F_name, L_name, emailid, password, state) => {
    var updatedUserDetails = userDetailsDB.push();

    updatedUserDetails.set({
        F_name : F_name,
        L_name : L_name,
        emailid : emailid,
        password : password,
        state : state
    })
}

const added_to_mailinglist = (newsletter) => {
    var updatedmailsSubscriptionDB = mailsSubscriptionDB.push();

    updatedmailsSubscriptionDB.set({
        newsletter : newsletter 
    })
}

const getElementVal = (id) =>{
    return document.getElementById(id).value;
};