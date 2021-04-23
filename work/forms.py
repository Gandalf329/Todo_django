from .models import Task
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['tittle', 'full_task', 'date']
        widgets = {
            "tittle": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Task name'
                }),
            "full_task": Textarea(attrs={
                'class':'form-control',
                'placeholder':'Task comment'
                }),
            "date": DateTimeInput(attrs={
                'class':'form-control',
                'placeholder':'Date'
                })
            
            }

