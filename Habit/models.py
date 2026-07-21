from django.db import models
from django.contrib.auth import get_user_model

from .exceptions import HabitAlreadyCompletedException, HabitAlreadyCanceledComplitionException


User = get_user_model()


class Habit(models.Model):
    title = models.CharField(max_length=200)
    complete_today = models.BooleanField(default=False)
    streak = models.IntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def complete(self):
        if self.complete_today:
            raise HabitAlreadyCompletedException("Привычка уже была отмечена сегодня")
        self.complete_today = True
        self.streak += 1
        self.save()
    
    def cancel_complition(self):
        if not self.complete_today:
            raise HabitAlreadyCanceledComplitionException("Привычка ещё не была отмечена")
        self.complete_today = False
        self.streak -= 1
        self.save()
    
    def reset_daily(self):
        if not self.complete_today:
            self.streak = 0
        self.complete_today = False
        self.save()
