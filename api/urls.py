from django.conf.urls import url

from api.views import AlbumList

app_name = "api"

urlpatterns = [
    url(r'^list_album/$', AlbumList.as_view()),
]