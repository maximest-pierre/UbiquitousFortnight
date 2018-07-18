from django.test import TestCase
from album.models import Genre
from album.factories import AlbumFactory, GenreFactory, RatingFactory

# Create your tests here.


class GenreTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.genre = GenreFactory()

    def test_name(self):
        self.assertEqual(self.genre.genre_name, "Test")


class AlbumTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.album = AlbumFactory()

    def test_album_name(self):
        self.assertNotEqual(self.album.album_name, "")

    def test_artist_name(self):
        self.assertNotEqual(self.album.artist_name, "")

    def test_released_date(self):
        self.assertNotEqual(self.album.released_date, "")

    def test_genre(self):
        self.assertNotEqual(self.album.genre.all(), "")

    def test_added_by(self):
        self.assertNotEqual(self.album.added_by.username, "")


class RatingTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.rating = RatingFactory()

    def test_user(self):
        self.assertNotEqual(self.rating.user.username, "")