from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class User(AbstractUser):
    username = None

    email = models.EmailField(max_length=150, unique=True, verbose_name='Email')
    telegram = models.CharField(max_length=150, verbose_name='telegram', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'
