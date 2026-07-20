from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class HabitsListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
    
    def test_habits_list_get(self):
        response = self.client.get(reverse('habits_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Habit/habits_list.html')

