let radioBtns = document.querySelectorAll("input[name='ST']");

let findSelected = () => {
    let selected = document.querySelector("input[name='ST']:checked").value;

    console.log(selected);
    if(selected == "Student"){
        document.getElementById("Roll_view").style.display="";
    }
    else if (selected == "Teacher"){
        document.getElementById("Roll_view").style.display="none";
    }
}


radioBtns.forEach(radioBtn => {
    radioBtn.addEventListener("change", findSelected);
});

findSelected();
