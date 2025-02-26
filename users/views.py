from rest_framework import generics
from .serializers import User, UserListSerializer
from rest_framework.permissions import IsAuthenticated


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]
