from django.shortcuts import render
from .models import Task

def all_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/all_tasks.html', {'tasks': tasks})

def important_tasks(request):
    tasks = Task.objects.filter(important=True)
    return render(request, 'tasks/important_tasks.html', {'tasks': tasks})

def completed_tasks(request):
    tasks = Task.objects.filter(completed=True)
    return render(request, 'tasks/completed_tasks.html', {'tasks': tasks})
