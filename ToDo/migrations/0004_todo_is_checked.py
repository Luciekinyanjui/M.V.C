# Generated by Django 2.2.5 on 2020-02-27 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0003_auto_20200221_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_checked',
            field=models.BooleanField(default=False),
        ),
    ]
