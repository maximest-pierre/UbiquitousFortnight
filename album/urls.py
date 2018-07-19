from django.conf.urls import url
from album.views import AlbumOverviewView

app_name = "album"

urlpatterns = [
    url(r'^overview', AlbumOverviewView.as_view())
]