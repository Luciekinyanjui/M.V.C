# Generated by Django 3.0.3 on 2020-05-09 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20200509_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='has_dark_mode',
        ),
    ]
