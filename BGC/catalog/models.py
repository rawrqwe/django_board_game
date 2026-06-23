from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


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

    min_players = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Za mało graczy."),
            MaxValueValidator(20, message="Za dużo graczy (maks. 20).")
        ]
    )
    max_players = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Za mało graczy."),
            MaxValueValidator(20, message="Za dużo graczy (maks. 20).")
        ]
    )

    min_time = models.IntegerField(
        validators=[
            MinValueValidator(5, message="Minimalny czas to 5 min"),
            MaxValueValidator(360, message="Maksymalny czas to 360 min")
        ]
    )
    max_time = models.IntegerField(
        validators=[
            MinValueValidator(5, message="Minimalny czas to 5 min"),
            MaxValueValidator(360, message="Maksymalny czas to 360 min")
        ]
    )

    min_age = models.IntegerField(
        validators=
        [MinValueValidator(3, message="Minimalny wiek to 3 lata"),
         MaxValueValidator(18, message="Maksymalny wiek to 18 lata")
         ]
    )

    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Review(models.Model):
    game = models.ForeignKey(BoardGame, on_delete=models.CASCADE, related_name="reviews")
    score = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    text = models.TextField()

    def __str__(self):
        return f"{self.game.title} - {self.score}"
