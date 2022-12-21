from django.contrib.auth.models import User
from .serializers import UserSerializer, UserListSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class UserViewSet(viewsets.ViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        queryset = User.objects.all().exclude(username="admin")
        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
                {"Error": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    # @action(detail=False, methods=["post"])
    # def login(self, request):
    #     username = request.data["username"]
    #     user = User.objects.get(username=username)
    #     if user is not None:
    #         login(request, user)
    #         token = Token.objects.get(user=user)
    #         return Response(
    #             {"message": "User '" + username + "' have logged in", "token": token.key},
    #             status=status.HTTP_200_OK,
    #         )
    #     else:
    #         return Response(
    #             "User '" + username + "' have not logged in",
    #             status=status.HTTP_400_BAD_REQUEST,
    #         )

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[IsAuthenticated],
        authentication_classes=[TokenAuthentication],
    )
    def logout(self, request):
        Token.objects.get(key=request.auth).delete()
        return Response(
            {"message": "You have logged out"},
            status=status.HTTP_200_OK,
        )
