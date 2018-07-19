from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import render, reverse

from album.models import Album


class AlbumOverviewView(LoginRequiredMixin, ListView):

    model = Album
    template_name = "album/overview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album

    fields = ['artist_name', 'album_name', 'released_date', 'genre', 'length']

    template_name = 'album/create_album.html'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        album = Album()
        if form.is_valid():
            album.artist_name = form.cleaned_data['artist_name']
            album.album_name = form.cleaned_data['album_name']
            album.released_date = form.cleaned_data['released_date']
            album.length = form.cleaned_data['length']
            album.added_by = request.user
            album.save()
            for item in form.cleaned_data['genre']:
                album.genre.add(item)

            return HttpResponseRedirect(self.get_success_url())

        else:
            return render(request, self.template_name, {'form': form})

    def get_success_url(self):
        return reverse('album:overview')
