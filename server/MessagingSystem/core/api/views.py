from rest_framework.response import Response
from rest_framework import viewsets, status
from core.models import Message
from .serializers import MessageSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class MessageViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]  # , BasicAuthentication
    permission_classes = [IsAuthenticated]

    def list(self, request):
        currUser = request.user
        unread = request.GET.get('unread', False)
        if unread:
            queryset = Message.objects.filter(receiver=currUser, unread=True).order_by(
                "-creation_date"
            )
        else:
            queryset = Message.objects.filter(receiver=currUser).order_by("-creation_date")
        serializer = MessageSerializer(queryset, many=True)
        for message in queryset:
            message.unread=False
            message.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        sender = User.objects.get(id=request.user.id)
        receiver = User.objects.get(username=request.data["receiver"])
        message = request.data["message"]
        subject = request.data["subject"]
        newMessage = Message(
            sender=sender, receiver=receiver, message=message, subject=subject
        )
        newMessage.save()
        return Response(
            {
                "message": "message id="
                + str(newMessage.id) 
                + " sent to "
                + receiver.username
                + "!"
            },
            status=status.HTTP_201_CREATED,
        )
    
    def retrieve(self, request, pk=None):
        message = Message.objects.filter(receiver=request.user).order_by('creation_date').last()
        serializer = MessageSerializer(message)
        message.unread=False
        message.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


    def destroy(self, request, pk=None):
        if pk is None:
            return Response(
                {"Error": "You have to provide message id!"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        message = get_object_or_404(Message, id=pk)
        if request.user == message.receiver or request.user == message.sender:
            message.delete()
            return Response({"message": "Message deleted!"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    "Error": "Access denied: you can't delete this message! Have to be owner or receiver."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
