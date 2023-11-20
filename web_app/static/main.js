var package_color = document.getElementById("package_color");
package_color.style.display = "none";

var bottle_cap = document.getElementById("bottle_cap");
bottle_cap.style.display = "none";

var reference = document.getElementById("reference"); 
reference.style.display = "none";

var capacity = document.getElementById("capacity"); 
capacity.style.display = "none";

var packaging_type = document.getElementById("packaging_type"); 
packaging_type.style.display = "none";

var dirtiness = document.getElementById("dirtiness"); 
dirtiness.style.display = "none";

var brand = document.getElementById("brand"); 
brand.style.display = "none";

var damage = document.getElementById("damage"); 
damage.style.display = "none";


function fadeOutEffect(idSubtipo, ...elements){
    var subtypeElement = document.getElementById(idSubtipo);
    console.log(idSubtipo);
    for(var i = 0; i < subtypeElement.length; i++){
        try {
            if(subtypeElement[i].value != undefined && subtypeElement[i].value != " "){
                for(var j = 0; j < elements.length; j++){
                    if(subtypeElement[i].value == elements[j]){
                        subtypeElement[i].style.display = "none";
                    }
                }
            }
        } catch (e) {
            break;
        }
    }
}


function fadeInEffect(idSubtipo, ...elements){
    var elementSelected = document.getElementById(idSubtipo);

    for(var i = 0; i < elementSelected.length; i++){
        try {
            if(elementSelected[i].value != undefined && elementSelected[i].value != " "){
                for(var j = 0; j < elements.length; j++){
                    if(elementSelected[i].value == elements[j]){
                        elementSelected[i].style.display = "block";
                    }
                }
            }
        } catch (e) {
            break;
        }
    }
}

var tipoSelect1 = document.getElementById("material");
console.log(tipoSelect1);
tipoSelect1.addEventListener("change", event => {
    var elementSelected2 = tipoSelect1.options[tipoSelect1.selectedIndex].value;
    console.log(elementSelected2);
    switch(elementSelected2){
        case "PET":
            package_color.style.display = "none";
            package_color.style.display = "block";
            fadeOutEffect("package_color", "N/A");
            fadeInEffect("package_color", "Clear transparent", "White transparent", "Red transparent", "Green transparent", "Brown transparent", "Blue transparent", "Colored transparent", "White opaque", "Blue opaque", "Green opaque", "Brown opaque", "Black opaque", "Colored opaque", "Yellow", "Orange", "Purple", "Gray", "Other color");
            break;
        case "PE-HD":
            package_color.style.display = "none";
            package_color.style.display = "block";
            fadeOutEffect("package_color", "N/A");
            fadeInEffect("package_color", "Clear transparent", "White transparent", "Red transparent", "Green transparent", "Brown transparent", "Blue transparent", "Colored transparent", "White opaque", "Blue opaque", "Green opaque", "Brown opaque", "Black opaque", "Colored opaque", "Yellow", "Orange", "Purple", "Gray", "Other color");
            break;
        case "PVC":
            package_color.style.display = "none";
            package_color.style.display = "block";
            fadeOutEffect("package_color", "N/A");
            fadeInEffect("package_color", "Clear transparent", "White transparent", "Red transparent", "Green transparent", "Brown transparent", "Blue transparent", "Colored transparent", "White opaque", "Blue opaque", "Green opaque", "Brown opaque", "Black opaque", "Colored opaque", "Yellow", "Orange", "Purple", "Gray", "Other color");
            break;
        case "PE-LD":
            package_color.style.display = "none";
            package_color.style.display = "block";
            fadeOutEffect("package_color", "N/A");
            fadeInEffect("package_color", "Clear transparent", "White transparent", "Red transparent", "Green transparent", "Brown transparent", "Blue transparent", "Colored transparent", "White opaque", "Blue opaque", "Green opaque", "Brown opaque", "Black opaque", "Colored opaque", "Yellow", "Orange", "Purple", "Gray", "Other color");
            break;
        case "PP":
            package_color.style.display = "none";
            package_color.style.display = "block";
            fadeOutEffect("package_color", "N/A");
            fadeInEffect("package_color", "Clear transparent", "White transparent", "Red transparent", "Green transparent", "Brown transparent", "Blue transparent", "Colored transparent", "White opaque", "Blue opaque", "Green opaque", "Brown opaque", "Black opaque", "Colored opaque", "Yellow", "Orange", "Purple", "Gray", "Other color");
            break;
        case "PS":
            package_color.style.display = "none";
            package_color.style.display = "block";
            fadeOutEffect("package_color", "N/A");
            fadeInEffect("package_color", "Clear transparent", "White transparent", "Red transparent", "Green transparent", "Brown transparent", "Blue transparent", "Colored transparent", "White opaque", "Blue opaque", "Green opaque", "Brown opaque", "Black opaque", "Colored opaque", "Yellow", "Orange", "Purple", "Gray", "Other color");
            break;
        case "Other plastic":
            package_color.style.display = "none";
            package_color.style.display = "block";
            fadeOutEffect("package_color", "N/A");
            fadeInEffect("package_color", "Clear transparent", "White transparent", "Red transparent", "Green transparent", "Brown transparent", "Blue transparent", "Colored transparent", "White opaque", "Blue opaque", "Green opaque", "Brown opaque", "Black opaque", "Colored opaque", "Yellow", "Orange", "Purple", "Gray", "Other color");
            break;
        case "Glass":
            package_color.style.display = "none";
            package_color.style.display = "block";
            fadeOutEffect("package_color", "N/A");
            fadeInEffect("package_color", "Clear transparent", "White transparent", "Red transparent", "Green transparent", "Brown transparent", "Blue transparent", "Colored transparent", "White opaque", "Blue opaque", "Green opaque", "Brown opaque", "Black opaque", "Colored opaque", "Yellow", "Orange", "Purple", "Gray", "Other color");
            break;
        case "Aluminium":
            package_color.style.display = "none";
            package_color.style.display = "block";
            packaging_type.style.display = "block";
            fadeInEffect("package_color", "N/A");
            fadeOutEffect("package_color", "Clear transparent", "White transparent", "Red transparent", "Green transparent", "Brown transparent", "Blue transparent", "Colored transparent", "White opaque", "Blue opaque", "Green opaque", "Brown opaque", "Black opaque", "Colored opaque", "Yellow", "Orange", "Purple", "Gray", "Other color");
            break;
        case "Other metal":
            package_color.style.display = "none";
            package_color.style.display = "none";
            package_color.style.display = "block";
            packaging_type.style.display = "block";
            fadeInEffect("package_color", "N/A");
            fadeOutEffect("package_color", "Clear transparent", "White transparent", "Red transparent", "Green transparent", "Brown transparent", "Blue transparent", "Colored transparent", "White opaque", "Blue opaque", "Green opaque", "Brown opaque", "Black opaque", "Colored opaque", "Yellow", "Orange", "Purple", "Gray", "Other color");
            break;
        case "Cardboard":
            package_color.style.display = "none";
            package_color.style.display = "block";
            packaging_type.style.display = "block";
            fadeInEffect("package_color", "N/A");
            fadeOutEffect("package_color", "Clear transparent", "White transparent", "Red transparent", "Green transparent", "Brown transparent", "Blue transparent", "Colored transparent", "White opaque", "Blue opaque", "Green opaque", "Brown opaque", "Black opaque", "Colored opaque", "Yellow", "Orange", "Purple", "Gray", "Other color");
            break;
        case "Paper print":
            package_color.style.display = "none";
            package_color.style.display = "block";
            packaging_type.style.display = "block";
            fadeInEffect("package_color", "N/A");
            fadeOutEffect("package_color", "Clear transparent", "White transparent", "Red transparent", "Green transparent", "Brown transparent", "Blue transparent", "Colored transparent", "White opaque", "Blue opaque", "Green opaque", "Brown opaque", "Black opaque", "Colored opaque", "Yellow", "Orange", "Purple", "Gray", "Other color");
            break;
        case "Newspaper":
            package_color.style.display = "none";
            package_color.style.display = "block";
            packaging_type.style.display = "block";
            fadeInEffect("package_color", "N/A");
            fadeOutEffect("package_color", "Clear transparent", "White transparent", "Red transparent", "Green transparent", "Brown transparent", "Blue transparent", "Colored transparent", "White opaque", "Blue opaque", "Green opaque", "Brown opaque", "Black opaque", "Colored opaque", "Yellow", "Orange", "Purple", "Gray", "Other color");
            break;
        case "Magazine":
            package_color.style.display = "block";
            packaging_type.style.display = "block";
            fadeInEffect("package_color", "N/A");
            fadeOutEffect("package_color", "Clear transparent", "White transparent", "Red transparent", "Green transparent", "Brown transparent", "Blue transparent", "Colored transparent", "White opaque", "Blue opaque", "Green opaque", "Brown opaque", "Black opaque", "Colored opaque", "Yellow", "Orange", "Purple", "Gray", "Other color");
            break;
        case "Tetrapack":
            package_color.style.display = "none";
            package_color.style.display = "block";
            packaging_type.style.display = "block";
            fadeInEffect("package_color", "N/A");
            fadeOutEffect("package_color", "Clear transparent", "White transparent", "Red transparent", "Green transparent", "Brown transparent", "Blue transparent", "Colored transparent", "White opaque", "Blue opaque", "Green opaque", "Brown opaque", "Black opaque", "Colored opaque", "Yellow", "Orange", "Purple", "Gray", "Other color");
            break;
        case "Other":
            package_color.style.display = "none";
            package_color.style.display = "block";
            packaging_type.style.display = "block";
            fadeInEffect("package_color", "N/A");
            fadeOutEffect("package_color", "Clear transparent", "White transparent", "Red transparent", "Green transparent", "Brown transparent", "Blue transparent", "Colored transparent", "White opaque", "Blue opaque", "Green opaque", "Brown opaque", "Black opaque", "Colored opaque", "Yellow", "Orange", "Purple", "Gray", "Other color");
            break;  
             
    }
});



var tipoSelect2 = document.getElementById("package_color");
console.log(tipoSelect3);
tipoSelect2.addEventListener("change", event => {

    packaging_type.style.display = "block";

});




var tipoSelect3 = document.getElementById("packaging_type");
console.log(tipoSelect3);
tipoSelect3.addEventListener("change", event => {
    var elementSelected3 = tipoSelect3.options[tipoSelect3.selectedIndex].value;
    console.log(elementSelected3);
    switch(elementSelected3){
        case "Bottle":
            bottle_cap.style.display = "none";
            bottle_cap.style.display = "block";
            fadeOutEffect("bottle_cap", "N/A");
            fadeInEffect("bottle_cap", "TRUE", "FALSE");
            fadeOutEffect("capacity", "N/A");
            fadeInEffect("capacity", "0-299","300-499","500-999","1000-1499","1500-3000",">3000");
            break
        case "Can":
            bottle_cap.style.display = "none";
            bottle_cap.style.display = "block";
            capacity.style.display = "block";
            fadeInEffect("bottle_cap", "N/A");
            fadeOutEffect("bottle_cap", "TRUE", "FALSE");
            fadeOutEffect("capacity", "N/A");
            fadeInEffect("capacity", "0-299","300-499","500-999","1000-1499","1500-3000",">3000");
            break
        case "Bag":
            bottle_cap.style.display = "none";
            bottle_cap.style.display = "block";
            capacity.style.display = "block";
            dirtiness.style.display = "block";
            fadeInEffect("bottle_cap", "N/A");
            fadeOutEffect("bottle_cap", "TRUE", "FALSE");
            fadeInEffect("capacity", "N/A");
            fadeOutEffect("capacity", "0-299","300-499","500-999","1000-1499","1500-3000",">3000");
            break
        case "Box":
            bottle_cap.style.display = "none";
            bottle_cap.style.display = "block";
            capacity.style.display = "block";
            fadeInEffect("bottle_cap", "N/A");
            fadeOutEffect("bottle_cap", "TRUE", "FALSE");
            fadeOutEffect("capacity", "N/A");
            fadeInEffect("capacity", "0-299","300-499","500-999","1000-1499","1500-3000",">3000");
            break
        case "Cup":
            bottle_cap.style.display = "none";
            bottle_cap.style.display = "block";
            fadeOutEffect("bottle_cap", "N/A");
            fadeInEffect("bottle_cap", "TRUE", "FALSE");
            fadeOutEffect("capacity", "N/A");
            fadeInEffect("capacity", "0-299","300-499","500-999","1000-1499","1500-3000",">3000");
            break
        case "Wrapping":
            bottle_cap.style.display = "none";
            bottle_cap.style.display = "block";
            capacity.style.display = "block";
            dirtiness.style.display = "block";
            fadeInEffect("bottle_cap", "N/A");
            fadeOutEffect("bottle_cap", "TRUE", "FALSE");
            fadeInEffect("capacity", "N/A");
            fadeOutEffect("capacity", "0-299","300-499","500-999","1000-1499","1500-3000",">3000");
            break
        case "Lid":
            bottle_cap.style.display = "none";
            bottle_cap.style.display = "block";
            capacity.style.display = "block";
            dirtiness.style.display = "block";
            fadeInEffect("bottle_cap", "N/A");
            fadeOutEffect("bottle_cap", "TRUE", "FALSE");
            fadeInEffect("capacity", "N/A");
            fadeOutEffect("capacity", "0-299","300-499","500-999","1000-1499","1500-3000",">3000");
            break
        case "Sheet":
            bottle_cap.style.display = "none";
            bottle_cap.style.display = "block";
            capacity.style.display = "block";
            dirtiness.style.display = "block";
            fadeInEffect("bottle_cap", "N/A");
            fadeOutEffect("bottle_cap", "TRUE", "FALSE");
            fadeInEffect("capacity", "N/A");
            fadeOutEffect("capacity", "0-299","300-499","500-999","1000-1499","1500-3000",">3000");
            break
        case "Other":
            bottle_cap.style.display = "none";
            bottle_cap.style.display = "block";
            capacity.style.display = "block";
            dirtiness.style.display = "block";
            fadeInEffect("bottle_cap", "N/A");
            fadeOutEffect("bottle_cap", "TRUE", "FALSE");
            fadeInEffect("capacity", "N/A");
            fadeOutEffect("capacity", "0-299","300-499","500-999","1000-1499","1500-3000",">3000");
            break      
             
    }
});


var tipoSelect4 = document.getElementById("bottle_cap");
console.log(tipoSelect4);
tipoSelect4.addEventListener("change", event => {
    var elementSelected4 = tipoSelect4.options[tipoSelect4.selectedIndex].value;
    console.log(elementSelected4);
            capacity.style.display = "block";

});


var tipoSelect5 = document.getElementById("capacity");
console.log(tipoSelect5);
tipoSelect5.addEventListener("change", event => {
    var elementSelected5 = tipoSelect5.options[tipoSelect5.selectedIndex].value;
    console.log(elementSelected5);
            dirtiness.style.display = "block";

});


var tipoSelect6 = document.getElementById("dirtiness");
console.log(tipoSelect6);
tipoSelect6.addEventListener("change", event => {
    var elementSelected6 = tipoSelect6.options[tipoSelect6.selectedIndex].value;
    console.log(elementSelected6);
            fadeOutEffect("brand", "N/A");
            brand.style.display = "block";

});


var tipoSelect7 = document.getElementById("brand");
console.log(tipoSelect7);
tipoSelect7.addEventListener("change", event => {
    var elementSelected7 = tipoSelect7.options[tipoSelect7.selectedIndex].value;
    console.log(elementSelected7);
    switch(elementSelected7){
        case "Coca-cola": 
            reference.style.display = "none";
            reference.style.display = "block";
            fadeOutEffect("reference", "N/A", "Manzana", "Pony Malta", "Yogurt", "Bonyurt", "Chocolatina Jet", "Pepsi");
            fadeInEffect("reference", "Original", "Zero", "Other");
            break 
        case "Bavaria":
            reference.style.display = "none";
            reference.style.display = "block";
            fadeOutEffect("reference", "N/A", "Zero", "Original", "Manzana", "Yogurt", "Bonyurt", "Chocolatina Jet", "Pepsi");
            fadeInEffect("reference", "Pony Malta", "Other");
            break 
        case "Postobon":
            reference.style.display = "none";
            reference.style.display = "block";
            fadeOutEffect("reference", "N/A", "Zero", "Original", "Pony Malta", "Yogurt", "Bonyurt", "Chocolatina Jet", "Pepsi");
            fadeInEffect("reference", "Manzana", "Other");
            break 
        case "Colanta": 
            reference.style.display = "none";
            reference.style.display = "block";
            fadeOutEffect("reference", "N/A", "Zero", "Original", "Pony Malta", "Manzana", "Chocolatina Jet", "Pepsi");
            fadeInEffect("reference", "Yogurt", "Bonyurt", "Other");
            break 
        case "Alpina": 
            reference.style.display = "none";
            reference.style.display = "block";
            fadeOutEffect("reference", "N/A", "Zero", "Original", "Pony Malta", "Manzana", "Chocolatina Jet", "Pepsi");
            fadeInEffect("reference", "Yogurt", "Bonyurt", "Other");
            break 
        case "Pepsi":
            reference.style.display = "none";
            reference.style.display = "block";
            fadeOutEffect("reference", "N/A", "Pony Malta", "Manzana", "Yogurt", "Bonyurt", "Chocolatina Jet", "Pepsi");
            fadeInEffect("reference", "Original", "Zero", "Other");
            break 
        case "Nacional de chocolates":
            reference.style.display = "none";
            reference.style.display = "block";
            fadeOutEffect("reference", "N/A", "Original", "Zero", "Pony Malta", "Manzana", "Yogurt", "Bonyurt", "Pepsi");
            fadeInEffect("reference", "Chocolatina Jet", "Other");
            break 
        case "Detodito": 
            reference.style.display = "none";
            reference.style.display = "block";
            fadeOutEffect("reference", "N/A", "Zero", "Pony Malta", "Manzana", "Yogurt", "Bonyurt", "Chocolatina Jet", "Pepsi");
            fadeInEffect("reference", "Original", "Other");
            break 
        case "Doritos":
            reference.style.display = "none";
            reference.style.display = "block";
            fadeOutEffect("reference", "N/A", "Zero", "Pony Malta", "Manzana", "Yogurt", "Bonyurt", "Chocolatina Jet", "Pepsi");
            fadeInEffect("reference", "Original", "Other");
            break 
        case "Gatorade":
            reference.style.display = "none";
            reference.style.display = "block";
            fadeOutEffect("reference", "N/A", "Zero", "Pony Malta", "Manzana", "Yogurt", "Bonyurt", "Chocolatina Jet", "Pepsi");
            fadeInEffect("reference", "Original", "Other");
            break 
        case "Cheesetris": 
            reference.style.display = "none";
            reference.style.display = "block";
            fadeOutEffect("reference", "N/A", "Zero", "Pony Malta", "Manzana", "Yogurt", "Bonyurt", "Chocolatina Jet", "Pepsi");
            fadeInEffect("reference", "Original", "Other");
            break 
        case "Manimoto":
            reference.style.display = "none";
            reference.style.display = "block";
            fadeOutEffect("reference", "N/A", "Zero", "Pony Malta", "Manzana", "Yogurt", "Bonyurt", "Chocolatina Jet", "Pepsi");
            fadeInEffect("reference", "Original", "Other");
            break 
        case "Margarita": 
            reference.style.display = "none";
            reference.style.display = "block";
            fadeOutEffect("reference", "N/A", "Zero", "Pony Malta", "Manzana", "Yogurt", "Bonyurt", "Chocolatina Jet", "Pepsi");
            fadeInEffect("reference", "Original", "Other");
            break 
        case "Tosh":
            reference.style.display = "none";
            reference.style.display = "block";
            fadeOutEffect("reference", "N/A", "Zero", "Pony Malta", "Manzana", "Yogurt", "Bonyurt", "Chocolatina Jet", "Pepsi");
            fadeInEffect("reference", "Original", "Other"); 
            break 
        case "Other":
            reference.style.display = "none";
            reference.style.display = "block";
            fadeOutEffect("damage", "N/A");
            damage.style.display = "block";
            fadeInEffect("reference", "N/A");
            fadeOutEffect("reference", "Zero", "Original", "Pony Malta", "Manzana", "Yogurt", "Bonyurt", "Chocolatina Jet", "Other", "Pepsi");
            break
    }
            

});


var tipoSelect8 = document.getElementById("reference");
console.log(tipoSelect8);
tipoSelect8.addEventListener("change", event => {
    var elementSelected8 = tipoSelect8.options[tipoSelect8.selectedIndex].value;
    console.log(elementSelected8);
    fadeOutEffect("damage", "N/A");
    damage.style.display = "block";

});
