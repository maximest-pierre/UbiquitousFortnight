from django.conf.urls import url
from album.views import AlbumCreateView, AlbumOverviewView, RatingCreateView, RatingDeleteView, RatingUpdateView

app_name = "album"

urlpatterns = [
    url(r'^overview', AlbumOverviewView.as_view(), name="overview"),
    url(r'^new', AlbumCreateView.as_view(), name="create"),
    url(r'^rating/new/(?P<album_id>\d+)', RatingCreateView.as_view(), name="new_rate"),
    url(r'^rating/update/(?P<pk>\d+)', RatingUpdateView.as_view(), name="update_rating"),
    url(r'^rating/delete/(?P<pk>\d+)', RatingDeleteView.as_view(), name="delete_rating"),
]