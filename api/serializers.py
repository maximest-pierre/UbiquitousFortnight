from album.models import Album, Rating
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('artist_name', 'album_name', 'released_date', 'genre', 'album_rating')

