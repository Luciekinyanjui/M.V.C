# Generated by Django 3.0.3 on 2020-03-17 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_has_dark_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sort_todos_by',
            field=models.CharField(default='date_added', max_length=100),
        ),
    ]
