# Generated by Django 2.2.5 on 2020-03-04 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0007_remove_todo_todos'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='due_date',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='past_due_date',
            field=models.BooleanField(default=False),
        ),
    ]
