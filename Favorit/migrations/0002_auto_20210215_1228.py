# Generated by Django 3.1.6 on 2021-02-15 08:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0007_music_songfile'),
        ('Favorit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritmusic',
            name='TimeFavorti',
            field=models.TimeField(default=datetime.time(12, 28, 54, 726695)),
        ),
        migrations.CreateModel(
            name='FavoritDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DetailFavortiUser', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Favorit.favoritmusic')),
                ('FavoritSong', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Music.music')),
            ],
        ),
    ]
