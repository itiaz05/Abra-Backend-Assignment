from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.views import obtain_auth_token


# Create your views here.
class UserViewSet(viewsets.ViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        username = request.data["username"]
        password = request.data["password"]
        serializer = UserSerializer(
            data={
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "password": password,
            }
        )
        if serializer.is_valid():
            userAcc = serializer.save()
            token = Token.objects.get(user=userAcc).key
            return Response(
                {
                    "message": "User have created",
                    "username": username,
                    "password": password,
                    "token": token,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {
                    "error": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(detail=False, methods=["post"])
    def login(self, request):
        username = request.data["username"]
        user = User.objects.get(username=username)
        if user is not None:
            login(request, user)
            token = Token.objects.get(user=user)
            return Response(
                {"message": "User '" + username + "' have logged in", "token": token.key},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                "User '" + username + "' have not logged in",
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(detail=False, methods=["get"])
    def logout(self, request):
        logout(request)
        return Response(
            "You have logged out",
            status=status.HTTP_200_OK,
        )
