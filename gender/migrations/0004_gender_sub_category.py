# Generated by Django 4.0 on 2021-12-23 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gender', '0003_remove_gender_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='gender',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_categoryies', to='gender.gender'),
        ),
    ]
