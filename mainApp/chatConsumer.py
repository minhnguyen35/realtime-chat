import json

from channels.generic.websocket import AsyncConsumer

class ChatConsumer(AsyncConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.channel_name}"
        print('connect to ', self.room_name)
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        await self.accept()

    #receive from web socket
    async def receive(self, message):
        msg_json = json.loads(message)
        msg = msg_json['message']
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": msg}
        )

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    #receive from room group
    async def chat_message(self, event):
        msg = event['message']
        await self.send(text_data = json.dumps({"message":msg}))