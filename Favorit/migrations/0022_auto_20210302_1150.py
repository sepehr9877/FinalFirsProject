# Generated by Django 3.1.6 on 2021-03-02 08:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Favorit', '0021_auto_20210302_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritmusic',
            name='TimeFavorti',
            field=models.TimeField(default=datetime.time(11, 50, 51, 525927)),
        ),
    ]
