from celery import shared_task
from .models import Habit

@shared_task
def reset_habits():
    updated = Habit.objects.filter(complete_today=True).update(complete_today=False)
    return f'Сброшено {updated} привычек'
