# Generated by Django 3.1.6 on 2021-02-23 08:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Favorit', '0006_auto_20210221_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritmusic',
            name='TimeFavorti',
            field=models.TimeField(default=datetime.time(12, 18, 57, 513358)),
        ),
    ]
