$(function () {
  const roomName = document.getElementById("room-name").textContent;
  const userName = document.getElementById("id_name").textContent;
  const body = document.getElementById("main_container");
  var prevUserName = null;

  const date = new Date();
  console.log(userName);

  const chatSocket = new WebSocket(
    "ws://" + window.location.host + "/ws/" + roomName + "/"
  );
  
  chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data).message;
    console.log(data);
    if (data.user_name != userName){
      const content = document.createElement('p');
      content.className='small p-2 ms-3 mb-1 rounded-3'
      content.style = 'background-color: #f5f6f7'
      content.textContent += data.message;
      if(!data.is_same_user) {
        body.insertAdjacentHTML('beforeend', '<br>');

        const newDiv = document.createElement('div');
        newDiv.className = 'd-flex justify-content-between';
        const name = document.createElement("p");
        name.className = 'small mb-1';
        name.textContent = data.user_name;

        const timestamp = document.createElement("p");
        timestamp.className = 'small mb-1 text-muted';
        timestamp.textContent = new Date().toLocaleTimeString();
        newDiv.insertAdjacentElement('afterbegin', timestamp);
        newDiv.insertAdjacentElement('afterbegin', name);

        body.insertAdjacentElement("beforeend", newDiv);

        const bodyMsgWrapper = document.createElement('div');
        const bodyMsg = document.createElement('div');
        // bodyMsg.id ='body_msg';
        bodyMsgWrapper.className = "d-flex flex-row justify-content-start";
        bodyMsgWrapper.insertAdjacentHTML('beforeend', `
          <img
          src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3-bg.webp"
          alt="avatar 1"
          style="width: 45px; height: 100%"
          />
        `)
        prevUserName = bodyMsg;
        prevUserName.insertAdjacentElement('beforeend', content);
        bodyMsgWrapper.insertAdjacentElement('beforeend', bodyMsg);
        body.insertAdjacentElement('beforeend', bodyMsgWrapper);
      }
      prevUserName.insertAdjacentElement('beforeend', content);
    } else {
      const content = document.createElement('p');
      content.className='small p-2 me-3 mb-1 text-white rounded-3 bg-primary'
      content.textContent += data.message;

      const timestampDiv = document.createElement('div');
      timestampDiv.className = 'd-flex justify-content-end';
       
      const timestampField = document.createElement('p');
      timestampField.className = 'small mb-1 text-muted';
      timestampField.textContent = new Date().toLocaleTimeString();
      timestampDiv.insertAdjacentElement('afterbegin', timestampField);
      
      if(!data.is_same_user) {
        const bodyMsgWrapper = document.createElement('div');
        const bodyMsg = document.createElement('div');
        bodyMsgWrapper.className = 'd-flex flex-row justify-content-end mb-4 pt-1';

        prevUserName = bodyMsg;
        bodyMsgWrapper.insertAdjacentElement('beforeend', bodyMsg);
        body.insertAdjacentElement('beforeend', timestampDiv);
        body.insertAdjacentElement('beforeend', bodyMsgWrapper);
      }
      prevUserName.insertAdjacentElement('beforeend', content);
    }
  };

  chatSocket.onclose = function (e) {
    console.error("Chat socket closed unexpectedly");
  };

  document.querySelector("#message_input").focus();
  document.querySelector("#message_input").onkeyup = function (e) {
    if (e.key === "Enter") {
      // enter, return
      document.querySelector("#message-submit").click();
    }
  };

  document.querySelector("#message-submit").onclick = function (e) {
    // const messageInputDom = document.querySelector("#message_input");
    // const message = messageInputDom.value;
    console.log(date.toLocaleString());
    var message = {
      user_name: userName,
      timestamp: date.toLocaleString(),
      message: $('#message_input').val(),
    }
    chatSocket.send(
      JSON.stringify({
        message: message,
      })
    );
    $('#message_input').val("");
  };
});
