from rest_framework import serializers
from .models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "telegram_chat_id", "email"]