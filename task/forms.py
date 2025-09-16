from django import forms 
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        exclude = ['user'] # model er kon kon field gula form e thakbe na
        # fields = [] model er kon kon field gula form e thakbe
        
        widgets = {
            'due_date' : forms.DateInput(attrs={'type' : 'date' }),
            'due_time' : forms.TimeInput(attrs={'type' : 'time' }),
        }