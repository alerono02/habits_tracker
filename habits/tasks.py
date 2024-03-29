from celery import shared_task

from habits.models import Habit
from users.services import tg_send_message


@shared_task
def habits_send_telegram(**kwargs):
    """Отправка напоминания о привычке"""
    habit = Habit.objects.get(pk=kwargs['pk'])
    tg_send_message(habit.user.telegram, str(habit))