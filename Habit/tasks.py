from celery import shared_task
from .models import Habit

@shared_task
def reset_habits():
    habits = Habit.objects.all()
    for habit in habits:
        habit.reset_daily()
    return f'Сброшено {len(habits)} привычек'
