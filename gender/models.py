from django.db import models


class Gender(models.Model):
    name = models.CharField(max_length=200, verbose_name='Пол')

    def __str__(self):
        return f'{self.name}'
