# Generated by Django 4.0 on 2021-12-23 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0015_personal_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='gender',
        ),
    ]
