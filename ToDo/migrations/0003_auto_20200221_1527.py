# Generated by Django 2.2.5 on 2020-02-21 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0002_auto_20200221_1526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='author',
            new_name='creator',
        ),
    ]
