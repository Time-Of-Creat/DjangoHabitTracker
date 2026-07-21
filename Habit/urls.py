from django.urls import path
from . import views

urlpatterns = [
    path('', views.habits_list, name='habits_list'),
    path('new/', views.HabitCreateView.as_view(), name='habit_create'),
    path("<int:pk>/edit/", views.HabitUpdateView.as_view(), name="habit_update"),
    path("<int:pk>/delete/", views.HabitDeleteView.as_view(), name="habit_delete"),
    path("<int:pk>/complete/", views.habit_complete, name="habit_complete"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
