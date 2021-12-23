# Generated by Django 4.0 on 2021-12-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gender', '0003_remove_gender_sub_category'),
        ('personal', '0009_remove_personal_gender_personal_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='gender',
        ),
        migrations.AddField(
            model_name='personal',
            name='gender',
            field=models.ManyToManyField(related_name='genders', to='gender.Gender'),
        ),
    ]
