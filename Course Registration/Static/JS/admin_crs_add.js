function GetSelectedValue(){
    
    let YearValue = document.getElementById("Year").value;
    let SemLength = document.getElementById("Semester").length;

    if (YearValue != "None" && SemLength == 1){
        let x = document.getElementById("Semester");
        const Sname = ["Odd","Even"];
        const Sval = ["Odd","Even"];
        
        for(i=0; i<Sname.length; i++){
            let option = document.createElement("option");
            option.value = Sval[i];
            option.text = Sname[i];
            x.add(option);
        }
    }
    else if (YearValue == "None"){
        document.getElementById("Semester").innerHTML = "";
        x = document.getElementById("Semester");
        option = document.createElement("option");
        option.value = "None";
        option.selected = true;
        option.disabled = true;
        option.text = "---";
        x.add(option);
    }
}

GetSelectedValue();
