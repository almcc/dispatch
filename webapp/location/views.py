from django.shortcuts import render
from location.models import Link, Tag
from django.db.models import Max


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