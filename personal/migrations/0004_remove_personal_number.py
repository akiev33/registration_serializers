# Generated by Django 4.0 on 2021-12-23 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_alter_personal_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='number',
        ),
    ]
