from django.shortcuts import render
from location.models import Link, Tag
from location.forms import LinkForm
from django.db.models import Max
from django.http import HttpResponseRedirect


def index(request):
    max = Tag.objects.all().aggregate(Max('column'))['column__max']
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

