# Generated by Django 4.0 on 2021-12-23 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gender', '0005_remove_gender_sub_category'),
        ('personal', '0010_remove_personal_gender_personal_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='gender',
        ),
        migrations.AddField(
            model_name='personal',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='genders', to='gender.gender'),
        ),
    ]
