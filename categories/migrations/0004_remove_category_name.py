# Generated by Django 4.0 on 2021-12-24 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_category_sub_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
    ]