# Generated by Django 4.2.7 on 2024-09-04 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_alter_todolist_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
