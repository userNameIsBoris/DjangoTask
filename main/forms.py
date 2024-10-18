from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class Task_form(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mt-2',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control mt-2',
                'placeholder': 'Введите описание'
            }),
        }
