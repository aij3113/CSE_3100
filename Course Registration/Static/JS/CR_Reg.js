
let radioBtns = document.querySelectorAll("input[name='ST']");

let findSelected = () => {
    let selected = document.querySelector("input[name='ST']:checked");

    if (selected.value == "Student") {
        document.getElementById("Roll_view").style.display = "";
        document.getElementById("roll").setAttribute("required","");
        document.getElementById("reg").setAttribute("required","");
        document.getElementById("series").setAttribute("required","");
        document.getElementById("section").setAttribute("required","");
    } 
    
    else if (selected.value == "Teacher") {
        document.getElementById("Roll_view").style.display = "none";
        document.getElementById("roll").removeAttribute("required");
        document.getElementById("reg").removeAttribute("required");
        document.getElementById("series").removeAttribute("required");
        document.getElementById("section").removeAttribute("required");

    }
}

radioBtns.forEach(radioBtn => {
    radioBtn.addEventListener("change", findSelected);
});

findSelected();
