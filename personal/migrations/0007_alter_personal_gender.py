# Generated by Django 4.0 on 2021-12-23 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gender', '0001_initial'),
        ('personal', '0006_alter_personal_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='genders', to='gender.gender'),
        ),
    ]
