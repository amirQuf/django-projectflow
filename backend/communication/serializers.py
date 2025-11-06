from .models import Message, ChatRoom
from rest_framework.serializers import ModelSerializer


class ChatRoomSerializer(ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = [
            "project",
            "team",
            "name",
            "created_at",
        ]


class MessageSerializer(ModelSerializer):
    room = ChatRoomSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ["room", "sender", "attachments", "content", "created_at"]
