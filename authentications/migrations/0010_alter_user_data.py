# Generated by Django 4.0 on 2021-12-24 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0009_user_age_user_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
    ]
