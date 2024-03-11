from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    PERIODIC_CHOICES = (
        ('s', 'Single'),
        ('d', 'Daily'),
        ('w', 'Weekly'),
        ('m', 'Monthly'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.DateTimeField(verbose_name='Время')
    action = models.CharField(max_length=255, verbose_name='действие')
    is_good_habit = models.BooleanField(default=False, verbose_name='признак приятной привычки', **NULLABLE)
    periodic = models.CharField(max_length=1, default='d', choices=PERIODIC_CHOICES, verbose_name='периодичность')
    lead_time = models.TimeField(verbose_name='время выполнения', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='публичный')
    reward = models.CharField(max_length=255, verbose_name='награда', **NULLABLE)
    associated_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка',
                                         **NULLABLE)

    def __str__(self):
        return f'Я буду {self.action} в {self.place} в {self.time}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
