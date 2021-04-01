from django.db import models

class BookShop(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=4)
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=150)
    year = models.CharField(max_length=4)
    date = models.DateField(auto_now_add=True)
    is_favorites = models.BooleanField(default=False)