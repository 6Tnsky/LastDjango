# films/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),  # Главная страница со списком фильмов
    path('add/', views.add_movie, name='add_movie'),  # Страница для добавления фильма
]
