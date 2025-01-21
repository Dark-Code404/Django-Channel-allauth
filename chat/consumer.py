import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from chat.models import *

from django.contrib.auth.models import User


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        self.room_name=self.room_name.replace('_'," ")

        print(self.room_name)
        

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = self.scope["user"].username

        

        room = Room.objects.get(name=self.room_name)
        user = User.objects.get(username=username)
        Message.objects.create(room=room, user=user, content=message)

        message=f"{username} : {message}"
        
        

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": message,"username": username,}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        username = self.scope["user"].username

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message,"username": username,}))