# Generated by Django 5.1.2 on 2024-10-18 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="usuario",
            name="bio",
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
