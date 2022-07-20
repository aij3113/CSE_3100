function GetSelectedValue(){
    let DeptValue = document.getElementById("department").value;
    let YearLength = document.getElementById("Year").length;

    if (DeptValue != "None" && YearLength == 1){
        let x = document.getElementById("Year");
        const Yname = ["1st","2nd","3rd","4th"];
        const Yval = ["1","2","3","4"];
        
        for(i=0; i<Yname.length; i++){
            let option = document.createElement("option");
            option.value = Yval[i];
            option.text = Yname[i];
            x.add(option);
        }
    
    }
    else if (DeptValue == "None"){
        document.getElementById("Year").innerHTML = "";
        x = document.getElementById("Year");
        option = document.createElement("option");
        option.value = "None";
        option.text = "---";
        x.add(option);
        
        document.getElementById("Semester").innerHTML = "";
        x = document.getElementById("Semester");
        option = document.createElement("option");
        option.value = "None";
        option.text = "---";
        x.add(option);
        
        document.getElementById("RS").innerHTML = "";
        x = document.getElementById("RS");
        option = document.createElement("option");
        option.value = "None";
        option.text = "---";
        x.add(option);
    }

    let YearValue = document.getElementById("Year").value;
    let SemLength = document.getElementById("Semester").length;

    if (YearValue != "None" && SemLength == 1){
        let x = document.getElementById("Semester");
        const Sname = ["Odd","Even"];
        const Sval = ["1","2"];
        
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
        option.text = "---";
        x.add(option);
        
        document.getElementById("RS").innerHTML = "";
        x = document.getElementById("RS");
        option = document.createElement("option");
        option.value = "None";
        option.text = "---";
        x.add(option);
    }

    let SemValue = document.getElementById("Semester").value;
    let RSLength = document.getElementById("RS").length;

    if(SemValue != "None" && RSLength == 1){
        let x = document.getElementById("RS");
        const RSname = ["Regular","Short"];
        const RSval = ["Regular","Short"];
        
        for(i=0; i<RSname.length; i++){
            let option = document.createElement("option");
            option.value = RSval[i];
            option.text = RSname[i];
            x.add(option);
        }
    }
    else if(SemValue == "None"){
        document.getElementById("RS").innerHTML = "";
        x = document.getElementById("RS");
        option = document.createElement("option");
        option.value = "None";
        option.text = "---";
        x.add(option);
    }
}

GetSelectedValue();
