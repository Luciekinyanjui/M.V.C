# Generated by Django 2.2.5 on 2020-03-21 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0011_subtask'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='num_of_subtasks',
            field=models.IntegerField(default=0),
        ),
    ]
