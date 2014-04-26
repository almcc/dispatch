from django.shortcuts import render
from location.models import Link, Tag
from location.forms import LinkForm, TagForm
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

    return render(request, 'location/index.html', {"columns": columns,
                                                   "column_class": "col-md-" + str(12//max)})

def newLink(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = LinkForm()
    return render(request, 'location/new-link.html', { 'form': form })

def editLink(request, linkId):
    instance = Link.objects.get(pk=linkId)
    if request.method == 'POST':
        form = LinkForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = LinkForm(instance=instance)
    return render(request, 'location/edit-link.html', { 'form': form, 'linkId': linkId})

def deleteLink(request, linkId):
    if request.method == 'POST':
        instance = Link.objects.get(pk=linkId)
        instance.delete()
    return HttpResponseRedirect('/')

def newTag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TagForm()
    return render(request, 'location/new-tag.html', { 'form': form })

def editTag(request, tagId):
    instance = Tag.objects.get(pk=tagId)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TagForm(instance=instance)
    return render(request, 'location/edit-tag.html', { 'form': form, 'tagId': tagId})

def deleteTag(request, tagId):
    if request.method == 'POST':
        instance = Tag.objects.get(pk=tagId)
        instance.delete()
    return HttpResponseRedirect('/')

def moveTagUp(request, tagId):
    instance = Tag.objects.get(pk=tagId)
    nextInstances = Tag.objects.filter(position=instance.position-1, column=instance.column)
    print instance
    print nextInstances
    if len(nextInstances) == 1:
        nextInstance = nextInstances[0]
        instance.position = instance.position - 1
        nextInstance.position = nextInstance.position + 1
        instance.save()
        nextInstance.save()
    return HttpResponseRedirect('/')

def moveTagDown(request, tagId):
    instance = Tag.objects.get(pk=tagId)
    nextInstances = Tag.objects.filter(position=instance.position+1, column=instance.column)
    print instance
    print nextInstances
    if len(nextInstances) == 1:
        nextInstance = nextInstances[0]
        instance.position = instance.position + 1
        nextInstance.position = nextInstance.position - 1
        instance.save()
        nextInstance.save()
    return HttpResponseRedirect('/')

def moveTagLeft(request, tagId):
    instance = Tag.objects.get(pk=tagId)
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
    return HttpResponseRedirect('/')

def moveTagRight(request, tagId):
    instance = Tag.objects.get(pk=tagId)
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
    return HttpResponseRedirect('/')

def getMaxPositionOfColumn(column):
    return Tag.objects.filter(column=column).aggregate(Max('position'))['position__max']

def reIndexColumn(column):
    tags = Tag.objects.order_by('position').filter(column = column)
    index = 1;
    for tag in tags:
        tag.position = index
        tag.save()
        index = index + 1







