from django import forms
from .models import Album
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['nombre','artista','genero','anio','portada']
