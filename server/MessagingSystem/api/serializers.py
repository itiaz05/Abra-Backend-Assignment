from rest_framework import serializers
from core.models import Message

class MessageSerializer(serializers.Serializer):
    class Meta:
        model = Message
        fields = '__all__'
