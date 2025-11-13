import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message
from .serializers import MessageSerializer
from django.contrib.auth.models import AnonymousUser


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.team_id = self.scope["url_route"]["kwargs"]["team_id"]
        self.room_group_name = f"team_{self.team_id}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

        messages = await self.get_last_messages()
        await self.send(json.dumps({"type": "history", "messages": messages}))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        content = data.get("content")
        user = self.scope.get("user")

        if not user or isinstance(user, AnonymousUser):
            await self.send(json.dumps({"error": "Authentication required"}))
            return

        message = await self.save_message(user, content)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
            },
        )

    async def chat_message(self, event):
        await self.send(
            text_data=json.dumps({"type": "message", "message": event["message"]})
        )

    @database_sync_to_async
    def save_message(self, user, content):
        msg = Message.objects.create(sender=user, team_id=self.team_id, content=content)
        return MessageSerializer(msg).data

    @database_sync_to_async
    def get_last_messages(self):
        messages = Message.objects.filter(team_id=self.team_id).order_by("-created_at")[
            :30
        ]
        return MessageSerializer(messages, many=True).data
