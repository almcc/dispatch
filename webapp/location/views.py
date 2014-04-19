from django.shortcuts import render
from location.models import Link


def index(request):
    links = Link.objects.all()
    return render(request, 'location/index.html', {"links": links})
