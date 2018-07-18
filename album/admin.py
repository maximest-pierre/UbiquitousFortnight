from django.contrib import admin
from album.models import Album, Genre, Rating

# Register your models here.

admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Rating)