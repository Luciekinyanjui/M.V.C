# Generated by Django 2.2.5 on 2020-03-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_sort_todos_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='total_todos',
            field=models.IntegerField(default=0),
        ),
    ]
