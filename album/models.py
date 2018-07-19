from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

from statistics import mean, StatisticsError


class Album(models.Model):
    class Meta:
        verbose_name_plural = "Albums"

    artist_name = models.CharField(max_length=200)
    album_name = models.CharField(max_length=200)
    released_date = models.DateField()
    genre = models.ManyToManyField('Genre')
    length = models.PositiveIntegerField()
    added_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_album"
    )

    def __str__(self):
        return "%s - %s" % (self.artist_name, self.album_name)

    def get_rating(self):
        ratings = self.album_rating.all()

        rating_list = []

        for rating in ratings:
            rating_list.append(rating.rating)

        try:
            return round(mean(rating_list), 1)
        except StatisticsError:
            return ""

    def get_genre(self):
        genres = self.genre.all()

        genre_list = []

        for genre in genres:
            genre_list.append(genre.genre_name)

        return ", ".join(genre_list)




class Genre(models.Model):
    class Meta:
        verbose_name_plural = "Genres"

    genre_name = models.CharField(max_length=200)

    def __str__(self):
        return self.genre_name


class Rating(models.Model):
    class Meta:
        verbose_name_plural = "Ratings"

    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="album_rating",
    )

    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_rating"
    )

    def __str__(self):
        return "%s - %s - %s" % (self.user.username, self.album.album_name, self.rating)