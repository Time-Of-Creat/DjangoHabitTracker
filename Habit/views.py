from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def habits_list(request):
    return render(request, 'Habit/habits_list.html')
