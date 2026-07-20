from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from ..models import Habit


User = get_user_model()


class HabitCreationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        self.create_url = reverse('habit_create')
    
    def test_create_habit_success(self):
        data = {
            'title': 'Утренняя зарядка'
        }

        self.assertEqual(Habit.objects.count(), 0)
        response = self.client.post(self.create_url, data)
        self.assertEqual(Habit.objects.count(), 1)

        habit = Habit.objects.first()

        self.assertEqual(habit.title, data['title'])
        self.assertEqual(habit.user, self.user)
        self.assertFalse(habit.complete_today)
        self.assertEqual(habit.streak, 0)
        self.assertIsNotNone(habit.creation_date)



