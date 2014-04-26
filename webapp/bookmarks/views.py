from django.shortcuts import render
from bookmarks.models import Link, Tag
from bookmarks.forms import LinkForm, TagForm
from django.db.models import Max
from django.http import HttpResponseRedirect


def index(request):
    max = Tag.objects.all().aggregate(Max('column'))['column__max']
    if max == None:
        max = 1
    if max > 6:
        max = 6

    columns = []
    for column in range(1,max+1):
        tags = Tag.objects.order_by('position').filter(column = column)
        tag_links = []
        for tag in tags:
            tag_links.append((tag, Link.objects.order_by('name').filter(tags__name = tag.name)))
        columns.append(tag_links)

    return render(request, 'bookmarks/index.html', {"columns": columns,
                                                   "column_class": "col-md-" + str(12//max)})

def newLink(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bookmarks/')
    else:
        form = LinkForm()
    return render(request, 'new-model.html', { 'form': form, 'modelPath': '/bookmarks/link' })

def editLink(request, modelId):
    instance = Link.objects.get(pk=modelId)
    if request.method == 'POST':
        form = LinkForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bookmarks/')
    else:
        form = LinkForm(instance=instance)
    return render(request, 'edit-model.html', { 'form': form, 'modelPath': '/bookmarks/link', 'modelId': modelId})

def deleteLink(request, modelId):
    if request.method == 'POST':
        instance = Link.objects.get(pk=modelId)
        instance.delete()
    return HttpResponseRedirect('/bookmarks/')

def newTag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bookmarks/')
    else:
        form = TagForm()
    return render(request, 'new-model.html', { 'form': form, 'modelPath': '/bookmarks/tag' })

def editTag(request, modelId):
    instance = Tag.objects.get(pk=modelId)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bookmarks/')
    else:
        form = TagForm(instance=instance)
    return render(request, 'edit-model.html', { 'form': form, 'modelPath': '/bookmarks/tag', 'modelId': modelId})

def deleteTag(request, modelId):
    if request.method == 'POST':
        instance = Tag.objects.get(pk=modelId)
        instance.delete()
    return HttpResponseRedirect('/bookmarks/')

def moveTagUp(request, modelId):
    instance = Tag.objects.get(pk=modelId)
    nextInstances = Tag.objects.filter(position=instance.position-1, column=instance.column)
    print instance
    print nextInstances
    if len(nextInstances) == 1:
        nextInstance = nextInstances[0]
        instance.position = instance.position - 1
        nextInstance.position = nextInstance.position + 1
        instance.save()
        nextInstance.save()
    return HttpResponseRedirect('/bookmarks/')

def moveTagDown(request, modelId):
    instance = Tag.objects.get(pk=modelId)
    nextInstances = Tag.objects.filter(position=instance.position+1, column=instance.column)
    print instance
    print nextInstances
    if len(nextInstances) == 1:
        nextInstance = nextInstances[0]
        instance.position = instance.position + 1
        nextInstance.position = nextInstance.position - 1
        instance.save()
        nextInstance.save()
    return HttpResponseRedirect('/bookmarks/')

def moveTagLeft(request, modelId):
    instance = Tag.objects.get(pk=modelId)
    oldColumn = instance.column
    newColumn = oldColumn - 1

    if newColumn >= 1:
        maxPosition = getMaxPositionOfColumn(newColumn)
        if maxPosition == None:
            maxPosition = 0
        instance.column = newColumn
        instance.position = maxPosition + 1
        instance.save()
        reIndexColumn(oldColumn)
    return HttpResponseRedirect('/bookmarks/')

def moveTagRight(request, modelId):
    instance = Tag.objects.get(pk=modelId)
    oldColumn = instance.column
    newColumn = oldColumn + 1
    if newColumn <= 6:
        maxPosition = getMaxPositionOfColumn(newColumn)
        if maxPosition == None:
            maxPosition = 0
        instance.column = newColumn
        instance.position = maxPosition + 1
        instance.save()
        reIndexColumn(oldColumn)
    return HttpResponseRedirect('/bookmarks/')

def getMaxPositionOfColumn(column):
    return Tag.objects.filter(column=column).aggregate(Max('position'))['position__max']

def reIndexColumn(column):
    tags = Tag.objects.order_by('position').filter(column = column)
    index = 1;
    for tag in tags:
        tag.position = index
        tag.save()
        index = index + 1







