# Generated by Django 4.1 on 2024-10-03 08:34

import cinema.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(null=True, upload_to=cinema.models.create_movie_media_upload_path),
        ),
    ]
