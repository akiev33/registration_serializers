# Generated by Django 4.0 on 2021-12-20 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=True, upload_to='image_product'),
        ),
    ]
