from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from core.settings import AUTH_USER_MODEL
from django.db.models import UniqueConstraint


class Post(models.Model):
    title = models.CharField(max_length=125)
    content = models.TextField()
    created_at = models.DateField(auto_now=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)


class Rating(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return self.user.username + str(self.rating)
    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'post'], name='rating_once')
        ]
