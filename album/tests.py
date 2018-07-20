from django.test import TestCase
from album.models import Album, Genre, Rating
from album.factories import AlbumFactory, GenreFactory, RatingFactory
from django.contrib.auth.models import User
from django.shortcuts import reverse
from urllib.parse import urlencode

import datetime


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


class AlbumCreateFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.admin = User.objects.create_superuser(
            username="admin@example.com",
            email="admin@example.com",
            password="test1234"
        )
        cls.genre = GenreFactory()

    def setUp(self):
        self.client.login(username=self.admin.username, password="test1234")

    def tearDown(self):
        self.client.logout()

    def test_access_to_form(self):
        result = self.client.get(
            reverse("album:create"),
            follow=True

        )
        self.assertEqual(result.status_code, 200)

    def test_form_save_data(self):
        data = {
            "artist_name": "Test",
            "album_name": "Test",
            "released_date": "2017-06-15",
            "length": 12,
            "genre": "1",
        }

        response = self.client.post(
            reverse("album:create"), data, follow=True,
        )
        album = Album.objects.get(album_name="Test")

        self.assertIsNotNone(album)


class RatingDeleteFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.admin = User.objects.create_superuser(
            username="admin@example.com",
            email="admin@example.com",
            password="test1234"
        )
        cls.rating = RatingFactory()

    def setUp(self):
        self.client.login(username=self.admin.username, password="test1234")

    def tearDown(self):
        self.client.logout()

    def test_access_to_form(self):
        result = self.client.get(
            reverse("album:delete_rating", args=(self.rating.id,)),
            follow=True
        )
        self.assertContains(result, 'Delete')

    def test_delete_form(self):
        result = self.client.post(
            reverse("album:delete_rating", args=(self.rating.id,)),
            follow=True
        )
        self.assertRedirects(result, reverse('album:overview'), status_code=302)


class RatingUpdateFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.admin = User.objects.create_superuser(
            username="admin@example.com",
            email="admin@example.com",
            password="test1234"
        )
        cls.rating = RatingFactory()

    def setUp(self):
        self.client.login(username=self.admin.username, password="test1234")

    def tearDown(self):
        self.client.logout()

    def test_access_to_form(self):
        result = self.client.get(
            reverse("album:update_rating", args=(self.rating.id,)),
            follow=True
        )
        self.assertContains(result, 'Edit')

    def test_update_form(self):

        data = {
            "rating": 8
        }
        result = self.client.post(
            reverse("album:update_rating", args=(self.rating.id,)),
            data,
            follow=True
        )

        self.assertRedirects(result, reverse('album:overview'), status_code=302)


class RatingCreateFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.admin = User.objects.create_superuser(
            username="admin@example.com",
            email="admin@example.com",
            password="test1234"
        )

        cls.album = AlbumFactory()

    def setUp(self):
        self.client.login(username=self.admin.username, password="test1234")

    def tearDown(self):
        self.client.logout()

    def test_access_to_form(self):
        result = self.client.get(
            reverse("album:new_rate", args=(self.album.id,)),
            follow=True
        )
        self.assertContains(result, 'Add')

    def test_create_form(self):
        data = {
            "rating": 8
        }
        result = self.client.post(
            reverse("album:new_rate", args=(self.album.id,)),
            data,
            follow=True
        )

        self.assertRedirects(result, reverse('album:overview'), status_code=302)