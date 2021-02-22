from django import forms
from .models import TaskModel


class TaskForm(forms.ModelForm):
    task = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))

    class Meta:
        model = TaskModel
        fields = ['task', ]

    def clean(self):
        cleaned_data = super(TaskForm, self).clean()
        task = cleaned_data.get('task')

        return cleaned_data
