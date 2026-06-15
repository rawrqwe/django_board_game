from django.shortcuts import render, get_object_or_404, redirect

from .forms import BoardGameForm, ReviewForm
from .models import BoardGame, Review

def game_main(request):
    return render(request, "catalog/game_main.html")

def game_list(request):
    games = BoardGame.objects.all()
    return render(request, "catalog/game_list.html", {"games": games})


def game_detail(request, pk):
    game = get_object_or_404(BoardGame, pk=pk)
    reviews = Review.objects.filter(game=game)
    return render(request, "catalog/game_detail.html", {
        "game": game,
        "reviews": reviews
    })


def game_create(request):
    if request.method == "POST":
        form = BoardGameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save()
            return redirect('game_detail', pk=game.pk)
    else:
        form = BoardGameForm()
    return render(request, 'catalog/game_form.html', {'form': form})


def add_review(request, pk):
    game = get_object_or_404(BoardGame, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)  # nie zapisuj jeszcze
            review.game = game  # przypisz grę do recenzji
            review.save()  # teraz zapisz
            return redirect('game_detail', pk=game.pk)
    else:
        form = ReviewForm()
    return render(request, 'catalog/review_form.html', {
        'form': form,
        'game': game,
    })
