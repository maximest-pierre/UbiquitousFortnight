from album.models import Album
from api.serializers import AlbumSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class AlbumList(APIView):

    @staticmethod
    def get(self):

        album = Album.objects.all()
        album_name = self.query_params.get('album_name', None)
        artist_name = self.query_params.get('artist_name', None)
        genre = self.query_params.get('genre', None)
        released_date = self.query_params.get('released_date', None)

        if album_name:
            album = album.filter(album_name__exact=str(album_name))

        if artist_name:
            album = album.filter(artist_name__exact=str(artist_name))

        if genre:
            album = album.filter(genre__genre_name__exact=str(genre))

        if released_date:
            album = album.filter(released_date__exact=released_date)

        return Response(AlbumSerializer(album, many=True).data)
