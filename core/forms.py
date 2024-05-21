from django import forms
from .models import Task

class SimpleForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important', 'completed']
