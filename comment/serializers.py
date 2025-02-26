from rest_framework import serializers
from .models import Comment


class CommentListCreateSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ["id",
                  "post",
                  "author",
                  "content",
                  "created_at", ]
