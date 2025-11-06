from .models import Message, ChatRoom
from rest_framework.viewsets import ModelViewSet
from .serializers import ChatRoomSerializer, MessageSerializer


class ChatroomViewSet(ModelViewSet):
    serializer_class = ChatRoomSerializer
    queryset = ChatRoom.objects.all()


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
