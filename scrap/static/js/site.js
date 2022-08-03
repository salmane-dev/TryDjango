const pushForm = document.getElementById('send-push__form');
const errorMsg = document.querySelector('.error');
const toko = document.querySelector('[name="csrfmiddlewaretoken"]').value 
 
pushForm.addEventListener('submit', async function (e) {
    e.preventDefault();
    const input = this[1];
    const textarea = this[2];
    const button = this[3];
    errorMsg.innerHTML = '';
    const msgs =  document.querySelector("#send-push__form > span")
    const head = input.value;
    const body = textarea.value
    const meta = document.querySelector('meta[name="user_id"]');
    const id = meta ? meta.content : null;
    console.log({head, body, id})

    if (head && body && id) {
        button.innerText = 'Sending...';
        button.disabled = true;

        const res = await fetch('../send_push', {
            method: 'POST',
            body: JSON.stringify({head, body, id}),
            headers: {
                'content-type': 'application/json',
                'Accept': 'application/json',
                'Content-Type': 'application/json; charset=UTF-8',
                //'X-CSRFToken': toko
            }
        });
        if (res.status === 200) { 
            console.log( " 200 == "+res.status)
            msgs.innerText = 'Send another 😃!';
            button.disabled = false;
            input.value = ''; 
            textarea.innerText = '';
        } else {
            console.log(res.status)
            console.log("50  50 5 50 50 50505 50")
            errorMsg.innerText = res.message;
            //button.innerText = 'Something broke 😢..  Try again?';
            button.disabled = false;
           //msgs.innerText = 'Something broke 😢..  Try again!';
        }
    }
    else {
        let error;
        if (!head || !body){
            error = 'Please ensure you complete the form 🙏🏾'
            msgs.innerText = error;
            console.log(res.status)
        }
        else if (!id){
            error = "Are you sure you're logged in? 🤔. Make sure! 👍🏼"
            msgs.innerText = '';
        }
        errorMsg.innerText = error;
        console.log(res.status)
    }    
});

 