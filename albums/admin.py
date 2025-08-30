from django.contrib import admin
from .models import Album
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display=('nombre','artista','genero','anio','creado_en')
    search_fields=('nombre','artista','genero')
