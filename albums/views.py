from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Album
from .forms import AlbumForm

class AlbumListView(ListView):
    model = Album
    template_name = 'albums/album_list.html'
    context_object_name = 'albums'
    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q','')
        if q:
            qs = qs.filter(Q(nombre__icontains=q)|Q(artista__icontains=q)|Q(genero__icontains=q)|Q(anio__icontains=q))
        return qs
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['q'] = self.request.GET.get('q','')
        return ctx

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'albums/album_detail.html'
    context_object_name = 'album'

class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album_list')
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creado_por = self.request.user
        obj.save()
        return super().form_valid(form)

class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album_list')

class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'albums/album_confirm_delete.html'
    success_url = reverse_lazy('album_list')
