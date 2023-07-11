const chatInput = document.getElementById("input-msg");
const sendChatbtn = document.querySelector(".chat-input span");
const chatbox = document.getElementById("msg-chat");
let userMessage;
//add login and register page prompt user to login if not exist register save their details
const createChatLi = (message, className) =>{
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat",className);
    let chatContent = className ==="outgoing" ? `<p>${message}</p>`: `<span class="material-symbols-outlined">smart_toy</span><p>${message}</p>`;
    chatLi.innerHTML = chatContent;
    return chatLi;
} 




const handleChat = ()=>{
    userMessage= chatInput.value;
    console.log(userMessage)
    if(!userMessage) return;
    chatbox.appendChild(createChatLi(userMessage,"outgoing"))
    //message to be generate
    if(userMessage=="hello") {
        if(veri()) {
            chatbox.appendChild(createChatLi("Login Successful","incoming"))
        }
    }
    chatInput.value="";
    

}

sendChatbtn.addEventListener("click",handleChat)
