from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.core.exceptions import ValidationError


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BoardGame(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    publisher = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='games/', blank=True)

    min_players = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    max_players = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    min_time = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    max_time = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    min_age = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(18)])

    genres = models.ManyToManyField(Genre)

    def clean(self):
        if self.min_players > self.max_players:
            raise ValidationError({
                "min_players": "Minimalna liczba graczy nie może być większa od maksymalnej."
            })

        if self.min_time > self.max_time:
            raise ValidationError({
                "min_time": "Minimalny czas gry nie może być większy od maksymalnego."
            })

    def __str__(self):
        return self.title


class Review(models.Model):
    game = models.ForeignKey(BoardGame, on_delete=models.CASCADE, related_name="reviews")
    score = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    text = models.TextField()

    def __str__(self):
        return f"{self.game.title} - {self.score}"
