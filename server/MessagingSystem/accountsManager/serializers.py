from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "first_name", "last_name"]

    def save(self):
        user = User(
            username=self.validated_data["username"],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
        )
        password = self.validated_data["password"]
        user.set_password(password)
        user.save()
        return user
