# Generated by Django 5.0.7 on 2024-08-03 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("memorialHall", "0003_memorialhall_creator"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="memorialhall",
            name="creator",
        ),
    ]
