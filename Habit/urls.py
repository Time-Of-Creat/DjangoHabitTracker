from django.urls import path
from . import views

urlpatterns = [
    path('', views.habits_list, name='habits_list'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
