from django.db import models
from django.db.models.fields import PositiveIntegerField


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BoardGame(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    publisher = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='brak opisu')
    image = models.ImageField(upload_to='games/', blank=True)

    min_players = models.IntegerField()
    max_players = models.IntegerField()
    min_time = models.IntegerField()
    max_time = models.IntegerField()
    min_age = models.IntegerField()

    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Review(models.Model):
    game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    score = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return f"{self.game.title} - {self.score}"