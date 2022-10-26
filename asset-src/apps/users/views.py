
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .renderer import UserJSONRenderer
from .serializers import UserSerializer

class UserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [UserJSONRenderer]

    def get(self, request):
        user = self.request.user
        print("THE USER")
        print(user)
        print(type(user))
        userall = User.objects.all()
        serializer = UserSerializer(userall, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)