from django import forms
from .models import BoardGame, Review

class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        exclude = ['id'] #pole które nie chce żeby było widać
        labels = {
            'title': 'Tytuł',
            'release_year': 'Rok wydania',
            'publisher': 'Wydawca',
            'description': 'Opis',
            'image': 'Okładka',
            'min_players': 'Minimalna liczba graczy',
            'max_players': 'Maksymalna liczba graczy',
            'min_time': 'Minimalny czas gry (minuty)',
            'max_time': 'Maksymalny czas gry (minuty)',
            'min_age': 'Minimalny wiek',
            'genres': 'Gatunki',
        }

        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': 'Wpisz opis gry...'
            })
        }

    def clean(self):
        cleaned_data = super().clean()

        min_players = cleaned_data.get("min_players")
        max_players = cleaned_data.get("max_players")

        min_time = cleaned_data.get("min_time")
        max_time = cleaned_data.get("max_time")

        # walidacja graczy
        if min_players and max_players:
            if min_players > max_players:
                self.add_error(
                    "min_players",
                    "Minimalna liczba graczy nie może być większa od maksymalnej."
                )

        # walidacja czasu gry
        if min_time and max_time:
            if min_time > max_time:
                self.add_error(
                    "min_time",
                    "Minimalny czas gry nie może być większy od maksymalnego."
                )

        return cleaned_data

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'score',
            'text',
        ]
        labels = {
            'score': 'Ocena',
            'text': 'Recenzja',
        }