const sendbtn = document.getElementById("sendbtn");
const chatinp = document.getElementById("msg");
const cbody = document.getElementById("cbody");
const messagesList = document.querySelector('.messages-list');
const messageForm = document.querySelector('.message-form');
const messageInput = document.querySelector('.message-input');
messageForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const message = messageInput.value.trim();

    const messageItem = document.createElement('li');
    messageItem.innerHTML = `<p>${message}</p>`;
    cbody.appendChild(messageItem);
    messageInput.value = '';

    fetch('', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        'message': message
      })
    })
      .then(response => response.json())
      .then(data => {
        const response = data.response;
        console.log(response.response);
        const messageItem = document.createElement('li');
        messageItem.innerHTML = `<p>${response}</p>`;
        cbody.appendChild(messageItem);
      });
  });
