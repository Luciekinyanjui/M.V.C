# Generated by Django 3.0.3 on 2020-05-01 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0014_todo_important'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='date_posted',
            new_name='date_created',
        ),
    ]
