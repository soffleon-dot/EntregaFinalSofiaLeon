from django.urls import path
from .views import AlbumListView, AlbumDetailView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView

urlpatterns = [
    path('catalogo/', AlbumListView.as_view(), name='album_list'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
    path('album/nuevo/', AlbumCreateView.as_view(), name='album_create'),
    path('album/<int:pk>/editar/', AlbumUpdateView.as_view(), name='album_update'),
    path('album/<int:pk>/eliminar/', AlbumDeleteView.as_view(), name='album_delete'),
]
