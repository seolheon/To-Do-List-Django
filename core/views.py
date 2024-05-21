from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, RedirectView, FormView
from .models import Task
from core import forms

class AllTasks(TemplateView):
    template_name = 'tasks/all_tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all()
        return context


class ImportantTasks(TemplateView):
    template_name = 'tasks/important_tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.filter(important=True)
        return context


class CompletedTasks(TemplateView):
    template_name = 'tasks/completed_tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.filter(completed=True)
        return context


class SimpleListView(ListView):
    template_name = 'tasks/simple_list_view.html'
    model = Task
    context_object_name = "tasks"


class SimpleDetailView(DetailView):
    template_name = 'tasks/simple_detail_view.html'
    model = Task
    context_object_name = "task"


class SimpleDetailView(DetailView):
    template_name = 'tasks/simple_detail_view.html'
    model = Task
    context_object_name = "task"


class SimpleRedirectView(RedirectView):
    query_string = True
    url = 'https://www.wikipedia.org/'


class SimpleFormView(FormView):
    template_name = 'tasks/form.html'
    form_class = forms.SimpleForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
