let side_button=document.querySelector("#change")
let side_bar=document.querySelector("#center")
let recent=document.querySelector("#unknown")
let recent_div=document.querySelector("#third")
let close_button=document.querySelector("#close")
let save_button=document.querySelector("#save")
let check=document.querySelector("#check")
let yes=document.querySelector("#yes")
let no=document.querySelector("#no")
let del_button=document.querySelector("#myybut")


side_button.addEventListener("click",change)
close_button.addEventListener("click",close_div)
recent.addEventListener("click",spread)
window.addEventListener("resize",shape)
save_button.addEventListener("click",to_recent)
del_button.addEventListener("click",confirm_delete)
no.addEventListener("click",cancel_delete)

function change(){
    if(side_bar.style.display=="none"){
        side_bar.style.display="block"
    }
    else{
        side_bar.style.display="none"
    }
}   

function spread(){
    console.log(77)
    console.log("Alive")
}

function close_div(){
    if(side_bar.style.display!="none"){
        side_bar.style.display="none"
    }
    if (recent_div.style.display=="none"){
        recent_div.style.display ="block"
    }
    else{
        recent_div.style.display="none"
    }
}

function to_recent(){
    recent_div.style.display="block"
}
function shape(){
    if (window.innerWidth >= 550){
        recent_div.style.display="block"
    }

    }
function confirm_delete(){
    if(check.style.display!="block"){
        check.style.display="block"
    }

}
function cancel_delete(){
    if(check.style.display!="none"){
        check.style.display="none"
    }
}