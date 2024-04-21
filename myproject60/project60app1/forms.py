from django import forms
from .models import Notemodel

class Noteform(forms.ModelForm):
    class Meta:
        model = Notemodel
        fields = ['title', 'author', 'publication_date']
