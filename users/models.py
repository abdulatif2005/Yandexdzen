from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.deconstruct import deconstructible



@deconstructible
class TgUsernameValidator:
    ALLOWED_CHARS = "ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0987654321_"
    code = "english"

    def __init__(self, message=None):
        self.message = message if message else "Accepted characters: A-z (case-insensitive), 0-9 and underscores. " \
                                               "Length: 5-32 characters."

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


# модель пользователя
class User(AbstractUser):
    telegram_chat_id = models.CharField(
        max_length=32,
        validators=[
            TgUsernameValidator(),
            MinLengthValidator(limit_value=5),
        ], blank=True
    )

    REQUIRED_FIELDS = ["email"]


