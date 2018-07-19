from django.conf.urls import url
from album.views import AlbumCreateView, AlbumOverviewView

app_name = "album"

urlpatterns = [
    url(r'^overview', AlbumOverviewView.as_view(), name="overview"),
    url(r'^new', AlbumCreateView.as_view(), name="create"),
]