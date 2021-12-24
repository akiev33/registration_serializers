# Generated by Django 4.0 on 2021-12-24 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_remove_category_sub_category'),
        ('products', '0007_alter_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='categories.category'),
        ),
    ]