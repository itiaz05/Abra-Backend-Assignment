from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    def create(self, request):
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        username = request.data["username"]
        password = "abra1234"
        serializer = UserSerializer(
            data={
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "password": password,
            }
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                "User " + request.data["username"] + " have created",
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                "Problem occurred creating User " + request.data["username"],
                status=status.HTTP_400_BAD_REQUEST,
            )

    def login(self, request):
        print(request.user)
        print(request.password)
        return Response(
            "User " + request.data["username"] + " have logged in",
            status=status.HTTP_200_OK,
        )
