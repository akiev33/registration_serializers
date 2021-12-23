from django.contrib.auth import get_user_model
from django.db import models

from gender.models import Gender

User = get_user_model()

class Personal(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='gen')
    age = models.PositiveIntegerField()
    number = models.IntegerField()
    author = models.ForeignKey(User, verbose_name='Личный кабинет',
                               on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} -- {self.id}'

