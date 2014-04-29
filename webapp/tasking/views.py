from django.shortcuts import render
from tasking.models import Task
from tasking.forms import TaskForm
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict


def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasking/index.html', {'tasks': tasks})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tasking/')
    else:
        form = TaskForm()
    return render(request, 'new-model.html', { 'form': form,
                                               'modelPath': '/tasking/task' })


def viewTask(request, modelId):
    instance = Task.objects.get(pk=modelId)
    model = model_to_dict(instance)
    return render(request, 'view-model.html', { 'model': model })


def editTask(request, modelId):
    instance = Task.objects.get(pk=modelId)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tasking/')
    else:
        form = TaskForm(instance=instance)
    return render(request, 'edit-model.html', { 'form': form,
                                                'modelPath': '/tasking/task',
                                                'modelId': modelId})

def deleteTask(request, modelId):
    if request.method == 'POST':
        instance = Task.objects.get(pk=modelId)
        instance.delete()
    return HttpResponseRedirect('/tasking/')