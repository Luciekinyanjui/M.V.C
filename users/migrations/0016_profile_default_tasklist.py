# Generated by Django 3.0.3 on 2020-05-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_profile_todos_completed_created_long_ago'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='default_tasklist',
            field=models.CharField(default='Unlisted', max_length=65),
        ),
    ]
