# Generated by Django 3.0.3 on 2020-05-01 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0015_auto_20200502_0017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='notes',
            new_name='has_notes',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='identification_id',
        ),
        migrations.RemoveField(
            model_name='subtask',
            name='identification_id',
        ),
        migrations.AlterField(
            model_name='notes',
            name='parent_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToDo.ToDo'),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='parent_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToDo.ToDo'),
        ),
    ]
