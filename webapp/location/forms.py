from django.forms import ModelForm
from location.models import Link

class LinkForm(ModelForm):
    class Meta:
        model = Link
