import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='почта')
    uid = models.UUIDField(default=uuid.uuid4, editable=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

