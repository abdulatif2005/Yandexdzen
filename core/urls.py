"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from djoser.views import UserViewSet, TokenCreateView, TokenDestroyView
from users.views import UserListAPIView
from post.views import PostListAPIView, PostCreateAPIView, PostRetrieveAPIView, RatePostAPIView
from comment.views import CommentCreateAPIView, CommentListAPIView, CommentUpdateDestroyAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/register/', UserViewSet.as_view({"post": "create"})),
    path('api/account/', UserListAPIView.as_view()),
    path('api/login/', TokenCreateView.as_view()),
    path('api/logout/', TokenDestroyView.as_view()),
    path('api/post/', PostListAPIView.as_view()),
    path('api/post/add/', PostCreateAPIView.as_view()),
    path('api/post/<int:post_id>/', PostRetrieveAPIView.as_view()),
    path('api/post/<int:post_id>/mark/add/', RatePostAPIView.as_view()),
    path('api/post/<int:post_id>/comment/', CommentListAPIView.as_view()),
    path('api/post/<int:post_id>/comment/add/', CommentCreateAPIView.as_view()),
    path('api/comment/<int:comment_id>/', CommentUpdateDestroyAPIView.as_view())
]
