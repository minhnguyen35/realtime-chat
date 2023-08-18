import json

from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.prevUser = None

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"
        print('connect to ', self.room_name)
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        await self.accept()

    #receive from web socket
    async def receive(self, text_data):
        msg_json = json.loads(text_data)
        msg = msg_json['message']
        print('message from browsers: ', msg)
        if self.prevUser is None or self.prevUser != msg['user_name']:
            msg['is_same_user'] = False
        else:
            msg['is_same_user'] = True
        self.prevUser = msg['user_name']
 
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": msg}
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    #receive from room group
    async def chat_message(self, event):
        msg = event['message']
        
        print('message from group: ', msg)
        await self.send(text_data = json.dumps({"message":msg}))