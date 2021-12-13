from django.db import models

from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    categories = models.ManyToManyField(Category, related_name='categories')

    def __str__(self):
        return f'{self.name}'
