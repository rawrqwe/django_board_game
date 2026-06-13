from django import forms
from .models import BoardGame, Review

class BoardGameForm(forms.BaseForm):
    class Meta:
        model = BoardGame
        exclude = ['id'] #pole które nie chce żeby było widać

class ReviewForm(forms.BaseForm):
    class Meta:
        model = Review
        fields = [
            'score',
            'text',
        ]
