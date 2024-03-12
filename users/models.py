from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class User(AbstractUser):

    username = models.CharField(unique=True, max_length=100, verbose_name="Никнейм")
    telegram = models.CharField(max_length=150, verbose_name='telegram', **NULLABLE)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'
