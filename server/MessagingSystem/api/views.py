from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getAllMessages():
    return Response({"message": "Hello, world!"})

