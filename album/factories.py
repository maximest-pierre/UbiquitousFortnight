import datetime
import random
from hashlib import md5

from django.contrib.auth.models import User
from album.models import Album, Genre, Rating

import factory


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = factory.Faker('first_name')

    email = factory.Sequence(lambda n: 'user{0}@example.com'.format(n))

    @classmethod
    def __prepare__(cls, create, **kwargs):
        password = 'test123'
        if 'password' in kwargs:
            password = kwargs.pop('password')
        user = super(UserFactory, cls).__prepare(create, **kwargs)
        user.set_password(password)
        if create:
            user.save()
        return user


class GenreFactory(factory.DjangoModelFactory):
    class Meta:
        model = Genre

    genre_name = "Test"


class AlbumFactory(factory.DjangoModelFactory):
    class Meta:
        model = Album

    artist_name = factory.Faker('first_name')
    album_name = factory.Faker('last_name')
    released_date = factory.Faker('date')
    length = factory.Faker('random_number')
    added_by = UserFactory()


class RatingFactory(factory.DjangoModelFactory):
    class Meta:
        model = Rating

    album = AlbumFactory()
    rating = factory.lazy_attribute(
        lambda x: random.randrange(1, 10)
    )
    user = UserFactory()