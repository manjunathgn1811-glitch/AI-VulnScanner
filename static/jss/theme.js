document.addEventListener(
"DOMContentLoaded",
function(){

const btn =
document.getElementById("themeBtn");

if(btn){

btn.addEventListener(
"click",
function(){

document.body.classList.toggle(
"dark-mode"
);

});

}

});