let room_button=document.querySelector("#rooms")
let message_button=document.querySelector("#messages")
let reply_button=document.querySelector("#replies")
let notification_button=document.querySelector("#notifications")
let search_div=document.querySelector("#top-search")


room_button.addEventListener("click",change_room)
message_button.addEventListener("click",change_message)
reply_button.addEventListener("click",change_reply)
notifications.addEventListener("click",change_notifications)
search_div.addEventListener("focus",display_button)
search_div.addEventListener("focusout",hide_button)

function change_room(){
    document.getElementById("messages-div").style.display="none"
    document.getElementById("replies-div").style.display="none"
    document.getElementById("notifications-div").style.display="none"
    document.getElementById("rooms-div").style.display="block"
}

function change_message(){
    document.getElementById("rooms-div").style.display="none"
    document.getElementById("replies-div").style.display="none"
    document.getElementById("notifications-div").style.display="none"
    document.getElementById("messages-div").style.display="block"
}

function change_reply(){
    document.getElementById("rooms-div").style.display="none"
    document.getElementById("notifications-div").style.display="none"
    document.getElementById("messages-div").style.display="none"
    document.getElementById("replies-div").style.display="block"
}
function change_notifications(){
    document.getElementById("rooms-div").style.display="none"
    document.getElementById("messages-div").style.display="none"
    document.getElementById("replies-div").style.display="none"
    document.getElementById("notifications-div").style.display="block"
}
function display_button(){
    document.getElementById("searchh").style.display="inline"
}
function hide_button(){
    document.getElementById("searchh").style.display="none"
}