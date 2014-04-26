from django.forms import ModelForm
from tasking.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
