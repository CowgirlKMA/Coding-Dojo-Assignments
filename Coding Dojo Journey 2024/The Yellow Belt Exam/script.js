//donate button
function hide(button){
    button.remove(button)
}
//alert when pet type is selected
function petChoice(value){
    alert("You are looking for a: "+value);
} 
// Pepper's pet count
var peppersCount=0;
var peppersPets=document.querySelector("#count");
    function pepper_add1(){
    peppersCount+=1;
    peppersPets.innerText=peppersCount+" pet(s) for Pepper!"; 
}  
// Bruce's pet count
var brucesCount=0;
var brucesPets=document.querySelector("#count2");
    function bruce_add1(){
    brucesCount+=1;
    brucesPets.innerText=brucesCount+" pet(s) for Bruce!"; 
}  
// Oscar's pet count
var oscarsCount=0;
var oscarsPets=document.querySelector("#count3");
    function oscar_add1(){
    oscarsCount+=1;
    oscarsPets.innerText=oscarsCount+" pet(s) for Oscar"; 
}   