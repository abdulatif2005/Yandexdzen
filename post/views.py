from django.db.models import Avg
from django.http import Http404
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Post, Rating
from .permissions import IsOwnerOrIsStaffOrReadOnly
from .serializers import PostListSerializer, PostCreateSerializer, RateSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        serializer.save()


class PostRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')
    serializer_class = PostListSerializer
    lookup_url_kwarg = "post_id"
    permission_classes = [IsOwnerOrIsStaffOrReadOnly]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return PostCreateSerializer
        return PostListSerializer


# class RatePostAPIView(AllowPUTAsCreateMixin, generics.UpdateAPIView):
#     serializer_class = RateSerializer
#     lookup_field = "post"
#     lookup_url_kwarg = "post_id"
#
#
#
#     def get_queryset(self):
#         user = self.request.user
#         return Rating.objects.filter(user=user)
#
#     def get_object(self):
#         queryset = self.get_queryset()
#         filter = {}
#         filter["post_id"] = self.kwargs[self.lookup_url_kwarg]
#         print(filter)
#         try:
#             obj = queryset.objects.get(post_id=filter["post_id"]).first()
#             print(obj)
#         except:
#             raise Http404
#         print(len(obj))
#         print(len(obj.user))
#         print(len(obj.post))
#         self.check_object_permissions(self.request, obj)
#         return obj
class RatePostAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RateSerializer
    lookup_url_kwarg = "post_id"

    def get_object(self):
        post_id = self.kwargs[self.lookup_url_kwarg]
        obj, created = Rating.objects.get_or_create(
            post_id=post_id, user=self.request.user, defaults={'rating': self.request.data.get('rating')}
        )
        return obj
