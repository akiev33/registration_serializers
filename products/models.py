from django.contrib.auth import get_user_model
from django.db import models

from categories.models import Category

User = get_user_model()

class Product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    categories = models.ManyToManyField(Category, related_name='categories')
    quantity = models.PositiveIntegerField()
    author = models.ForeignKey(User, verbose_name='Автор поста',
                               on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name} -- {self.id}'
