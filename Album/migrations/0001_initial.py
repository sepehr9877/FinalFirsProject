# Generated by Django 3.1.6 on 2021-02-08 18:07

import Album.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.CharField(default='2000', max_length=150)),
                ('AlbumName', models.CharField(default='unknown', max_length=150)),
                ('AlbumImage', models.ImageField(upload_to=Album.models.upload_image)),
            ],
        ),
    ]
