from rest_framework import generics
from .serializers import CommentListCreateSerializer, Comment
from .permissions import IsStaffOrReadOnly


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentListCreateSerializer
    lookup_url_kwarg = "post_id"

    def get_queryset(self):
        post_id = self.kwargs[self.lookup_url_kwarg]
        quryset = Comment.objects.filter(post_id=post_id)
        return quryset


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentListCreateSerializer
    lookup_url_kwarg = "post_id"

    def perform_create(self, serializer):
        serializer.save(post_id=self.kwargs[self.lookup_url_kwarg])


class CommentUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListCreateSerializer
    lookup_url_kwarg = "comment_id"
    permission_classes = [IsStaffOrReadOnly]
