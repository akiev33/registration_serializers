# Generated by Django 4.0 on 2021-12-24 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_remove_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=0, max_length=200, verbose_name='Категории'),
            preserve_default=False,
        ),
    ]
