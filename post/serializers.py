from rest_framework import serializers
from .models import Post, Rating


class PostListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.IntegerField()

    class Meta:
        model = Post
        fields = "__all__"


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "created_at", "user"]


class RateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Rating
        fields = ["rating", "post", "user"]
