# Generated by Django 3.0.3 on 2020-05-17 16:52

import ToDo.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0018_todo_parent_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.FileField(blank=True, help_text='Add important documents or pictures', null=True, upload_to=ToDo.models.get_attachment_dir)),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('parent_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToDo.ToDo')),
            ],
        ),
    ]
