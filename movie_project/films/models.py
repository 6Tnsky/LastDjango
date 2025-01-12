# films/models.py
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)  # Название фильма
    description = models.TextField()  # Описание фильма
    review = models.TextField()  # Отзыв

    def __str__(self):
        return self.title

