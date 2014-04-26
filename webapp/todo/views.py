from django.shortcuts import render
from todo.models import Task
from todo.forms import TaskForm
from django.http import HttpResponseRedirect

def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/todo/')
    else:
        form = TaskForm()
    return render(request, 'new-model.html', { 'form': form,
                                               'modelPath': '/todo/task' })

def editTask(request, modelId):
    instance = Task.objects.get(pk=modelId)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/todo/')
    else:
        form = TaskForm(instance=instance)
    return render(request, 'edit-model.html', { 'form': form,
                                                'modelPath': '/todo/task',
                                                'modelId': modelId})

def deleteTask(request, modelId):
    if request.method == 'POST':
        instance = Task.objects.get(pk=modelId)
        instance.delete()
    return HttpResponseRedirect('/todo/')