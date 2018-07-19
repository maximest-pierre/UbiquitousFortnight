from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from album.models import Album


class AlbumOverviewView(LoginRequiredMixin, ListView):

    model = Album
    template_name = "album/overview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
