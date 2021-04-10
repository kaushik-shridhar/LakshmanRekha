# model form
from django import forms
from .models import *

class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ['name', 'upload_locn']