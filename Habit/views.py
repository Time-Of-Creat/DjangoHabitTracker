from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import Habit
from .exceptions import HabitAlreadyCompletedException


class HabitCreateView(LoginRequiredMixin, CreateView):
    model = Habit
    fields = ['title',]
    template_name = 'Habit/habit_form.html'
    success_url = reverse_lazy('habits_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class HabitUpdateView(LoginRequiredMixin, UpdateView):
    model = Habit
    fields = ['title',]
    template_name = 'Habit/habit_form.html'
    success_url = reverse_lazy('habits_list')

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitDeleteView(LoginRequiredMixin, DeleteView):
    model = Habit
    template_name = 'Habit/habit_delete.html'
    success_url = reverse_lazy('habits_list')

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


@login_required
def habit_complete(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    try:
        habit.complete()
    except HabitAlreadyCompletedException:
        messages.error(request, f"Привычка {habit} уже была отмечена сегодня!")
    
    return redirect('habits_list')


@login_required
def habit_cancel(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    try:
        habit.cancel_complition()
    except HabitAlreadyCompletedException:
        messages.error(request, f"Привычка {habit} уже была отмечена сегодня!")
    
    return redirect('habits_list')


@login_required
def habits_list(request):
    habits = Habit.objects.filter(user=request.user).order_by('-creation_date')
    return render(request, 'Habit/habits_list.html', {'habits': habits})
