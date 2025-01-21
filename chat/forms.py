from .models import *
from django import forms

from django.forms import ModelForm


class RoomCreate(forms.ModelForm):
    class Meta:
        model=Room
        fields = ['name', 'description']
        
    





