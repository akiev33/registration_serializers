# Generated by Django 4.0 on 2021-12-23 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0017_alter_personal_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personal',
            old_name='author',
            new_name='person',
        ),
    ]