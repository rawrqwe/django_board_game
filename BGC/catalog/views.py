from django.shortcuts import render, get_object_or_404
from .models import BoardGame, Review


def game_list(request):
    games = BoardGame.objects.all()
    return render(request, "catalog/game_list.html",{"games": games})


def game_detail(request, pk):
    game = get_object_or_404(BoardGame, pk=pk)
    reviews = Review.objects.filter(game=game)
    return render(request, "catalog/game_deatail.html",{
        "game": game,
        "reviews": reviews
    })

def game_create(request):
    pass