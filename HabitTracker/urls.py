from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/habits/')),
    path('habits/', include("Habit.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls"))
]
