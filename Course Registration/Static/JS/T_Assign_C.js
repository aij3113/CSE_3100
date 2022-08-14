function selectUnselectAll(){
    let sAll = document.getElementsByName("checkAll");
    
    if(sAll.checked == true){
        var rolls = document.getElementsByName("Rolls");
        for(var i=0; i<rolls.length; i++){
            if(rolls[i].checked == false){
                rolls[i].checked = true;
            }
        }
        document.getElementById("nselected").innerHTML = "( " + rolls.length + " Selected)";
        sAll.checked = false;
    }

    else{
        var rolls = document.getElementsByName("Rolls");
        for(var i=0; i<rolls.length; i++){
            if(rolls[i].checked == true){
                rolls[i].checked = false;
            }
        }
        document.getElementById("nselected").innerHTML = "( 0 Selected)";
        sAll.checked = true;
    }


}

selectUnselectAll();

function ncount(){
    var roll = document.getElementsByName("Rolls");

    var x = 0;

    for (var i = 0; i<roll.length; i++){
        if (roll[i].checked == true){
            x+=1;
        }
    }

    if(x == roll.length ){
        let cAll = document.getElementsByName("checkAll");
        if(cAll.checked == false){
            cAll.checked = true;
        }
    }
    document.getElementById("nselected").innerHTML = "( "+ x + " Selected)";
}

ncount();