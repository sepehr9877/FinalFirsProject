# Generated by Django 3.1.6 on 2021-03-07 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Favorit', '0044_auto_20210307_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritmusic',
            name='TimeFavorti',
            field=models.DateTimeField(default=datetime.time(18, 44, 32, 840712)),
        ),
    ]
