from rest_framework.response import Response

# from rest_framework.decorators import api_view
from rest_framework import viewsets, status
from core.models import Message
from .serializers import MessageSerializer
from django.contrib.auth.models import User


class MessageViewSet(viewsets.ViewSet):
    def list(self, request):
        currUser = request.user
        queryset = Message.objects.filter(receiver=currUser).order_by("-creation_date")
        serializer = MessageSerializer(queryset, many=True)
        queryset.update(unread=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        sender = User.objects.get(id=request.user.id)
        receiver = User.objects.get(id=request.data["receiver"])
        message = request.data["message"]
        subject = request.data["subject"]
        newMessage = Message(
            sender=sender, receiver=receiver, message=message, subject=subject
        )
        newMessage.save()
        return Response(
            {
                "message": "Message sent to "
                + receiver.first_name
                + " "
                + receiver.last_name
                + "!"
            },
            status=status.HTTP_201_CREATED,
        )

    def destroy(self, request, pk=None):
        message = Message.objects.get(id=pk)
        if request.user == message.receiver or request.user == message.sender:
            message.delete()
            return Response({"message": "Message deleted!"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    "message": "You can't delete this message! \n Have to be owner or receiver."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
