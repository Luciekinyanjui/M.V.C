# Generated by Django 2.2.5 on 2020-04-06 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_remove_profile_last_insights_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_insights_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
