# Generated by Django 5.0.3 on 2024-04-15 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="lien",
            field=models.CharField(default="hey", max_length=256),
            preserve_default=False,
        ),
    ]
