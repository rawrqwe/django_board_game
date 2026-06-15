from django.contrib import admin
from .models import BoardGame, Genre, Review

admin.site.register(BoardGame)
admin.site.register(Genre)
admin.site.register(Review)
