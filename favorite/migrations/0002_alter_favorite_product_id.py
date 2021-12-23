# Generated by Django 4.0 on 2021-12-22 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_image'),
        ('favorite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_favorite', to='products.product'),
        ),
    ]
