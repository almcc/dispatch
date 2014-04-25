from django.forms import ModelForm
from location.models import Link, Tag

class LinkForm(ModelForm):
    class Meta:
        model = Link

class TagForm(ModelForm):
    class Meta:
        model = Tag
