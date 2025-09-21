from django import forms
from .models import MovieModel

class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieModel
        fields = ['name', 'director', 'year']