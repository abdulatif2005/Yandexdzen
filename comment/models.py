from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from post.models import Post


# # Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment")  # •	пост
    author = models.CharField(max_length = 32, validators=[MinLengthValidator(5)])         # •	автор (имя автора комментария)
    content = models.TextField(validators=[MinLengthValidator(5), MaxLengthValidator(500)])# •	текст комментария
    created_at = models.DateField(auto_now_add=True)                                       # •	дата публикации

    def __str__(self):
        return self.author + " " + self.content
