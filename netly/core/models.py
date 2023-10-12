from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT, related_name="movies")
    numberInStock = models.IntegerField()
    dailyRentalRate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return self.title
