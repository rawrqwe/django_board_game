from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_main, name='game_main'),
    path('game_list/', views.game_list, name='game_list'),
    path('<int:pk>/', views.game_detail, name='game_detail'),
    path('create/', views.game_create, name='game_create'),
    path('<int:pk>/review/', views.add_review, name='add_review'),
    path('<int:pk>/reviews/',views.game_reviews, name='game_reviews'),
    path('<int:pk>/delete/', views.game_delete, name='game_delete'),

]
