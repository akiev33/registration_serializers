from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product

User = get_user_model()

class Basket(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_basket')
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_basket')
    count = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.product_id} - {self.user_id} {self.total}'