from django.contrib.auth.models import AbstractUser
from django.db import models


class Publication(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Genre(models.Model):
    genre = models.CharField(max_length=63)

    def __str__(self):
        return self.genre


class Author(AbstractUser):

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"


class Book(models.Model):
    title = models.CharField(max_length=255)
    pub_house = models.ForeignKey(Publication, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="authors")
    price = models.IntegerField()

    def __str__(self):
        return f"{self.title}: {self.genre}"
