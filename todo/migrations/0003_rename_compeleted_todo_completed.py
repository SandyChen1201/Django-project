# Generated by Django 5.0.3 on 2024-03-26 12:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0002_todo_compeleted"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todo",
            old_name="compeleted",
            new_name="completed",
        ),
    ]
