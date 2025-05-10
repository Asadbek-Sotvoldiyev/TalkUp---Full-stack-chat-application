from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
from .models import ChatGroup, Message
from users.models import User
from .crypto import encrypt_message, decrypt_message
import json


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['name']
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()
        await self.channel_layer.group_send(self.room_name, {"type": "fetch_history"})

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        time = await self.create_messages(message=text_data_json['message'], sender_id=text_data_json['sender_id'])

        await self.channel_layer.group_send(
            self.room_name,
            {
                "type": "chat_message",
                "message": text_data_json['message'],
                "sender_id": text_data_json['sender_id'],
                "time": time
            }
        )

    async def chat_message(self, event):

        await self.send(
            text_data=json.dumps(
                {
                    "message": event['message'],
                    "sender_id": event['sender_id'],
                    "time": event['time']
                }
            )
        )

    @database_sync_to_async
    def create_messages(self, message, sender_id):
        chat_group = ChatGroup.objects.get(name=self.room_name)
        sender = User.objects.get(id=sender_id)
        message = Message.objects.create(
            body=encrypt_message(message),
            sender=sender,
            chatgroup=chat_group,
        )

        return message.time.strftime("%h-%d %H:%M")

    async def fetch_history(self, event):
        messages = await self.history_messages()
        for message in messages:
            await self.send(text_data=json.dumps(message))


    @database_sync_to_async
    def history_messages(self):
        chat_group = ChatGroup.objects.get(name=self.room_name)
        messages = Message.objects.filter(chatgroup=chat_group)

        serialized_messages = [
            {
                "message": decrypt_message(message.body),
                "sender_id": message.sender.id,
                "time": message.time.strftime("%h-%d %H:%M")
            } for message in messages
        ]
        return serialized_messages



