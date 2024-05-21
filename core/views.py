from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Task

class AllTasks(TemplateView):
    tasks = Task.objects.all()
    template_name = 'tasks/all_tasks.html'

class ImportantTasks(TemplateView):
    tasks = Task.objects.filter(important=True)
    template_name = 'tasks/important_tasks.html'

class CompletedTasks(TemplateView):
    tasks = Task.objects.filter(completed=True)
    template_name ='tasks/completed_tasks.html'
