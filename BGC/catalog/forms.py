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