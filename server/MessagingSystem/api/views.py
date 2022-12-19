from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.decorators import action
from core.models import Message
from .serializers import MessageSerializer, UserSerializer
from django.contrib.auth.models import User

class MessageViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Message.objects.all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        sender = User.objects.get(id=request.data['sender'])
        receiver = User.objects.get(id=request.data['receiver'])
        message = request.data['message']
        subject = request.data['subject']
        newMessage = Message(sender=sender, receiver=receiver, message=message, subject=subject)
        newMessage.save()
        return Response({"message": "Message sent to " + receiver.first_name + " " + receiver.last_name + "!"})

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

## This is the old way of doing things
# @api_view(['GET'])
# def getAllMessages():
#     return Response({"message": "Hello, world!"})

