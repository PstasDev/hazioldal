const csrftoken = getCookie('csrftoken');
document.addEventListener("DOMContentLoaded", main);
document.addEventListener("DOMContentLoaded", checkbox);

function main(){
    ovatos_esemenykapcsolas('#update', 'click', update_git);
}

//////////////////////////////////////

// UPDATE
async function update_git() {
    let url = `${window.location.origin}/${hazioldalurl()}/api/post/git/update/`;
    let szotar = {
        'username': document.querySelector('#gitusername').value,
    };
    try {
        let res = await kuldo_fetch(url, szotar);
        if (res && !res.title && res.message) {
            openModal('Response', res.message);
        } else if (res && res.title && res.message) {
            openModal(res.title, res.message);
        } else if (res && res.title && !res.message) {
            openModal(res.title, "Hiba az üzenet megjelnítése során");
        } else {
            throw new Error('Invalid response from server');
        }
    } catch (error) {
        console.error('Error occurred while updating Git:', error);
        openModal('Error', 'An error occurred while updating Git');
    }
}

function openModal(title, message) {
    gitmodalTitle.textContent = title;
    gitmodalMessage.textContent = message;

    git_username_updated.showModal();
}

function CommitChange(){
    var elem = document.getElementById('check1');
    if (elem.checked){
        localStorage.setItem("ShowCommitHistory", "on");
        console.info("ShowCommitHistory changed to: on");
    }
    else
    {
        localStorage.setItem("ShowCommitHistory", "off");
        console.info("ShowCommitHistory changed to: off");
    }
}

function checkbox(){
    var checked = localStorage.getItem("ShowCommitHistory");
    if (checked =="on"){
        document.getElementById("check1").checked = true;
    }
    else{
        document.getElementById("check1").checked = false;
    }
}
