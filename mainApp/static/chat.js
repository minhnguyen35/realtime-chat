$(function () {
  const roomName = JSON.parse(document.getElementById("room-name").textContent);

  const chatSocket = new WebSocket(
    "ws://" + window.location.host + "/ws/chat/" + roomName + "/"
  );

  chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    document.querySelector("#chat-log").value += data.message + "\n";
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
    const messageInputDom = document.querySelector("#message_input");
    const message = messageInputDom.value;
    chatSocket.send(
      JSON.stringify({
        message: message,
      })
    );
    messageInputDom.value = "";
  };
});
