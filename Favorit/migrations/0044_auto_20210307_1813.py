# Generated by Django 3.1.6 on 2021-03-07 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Favorit', '0043_auto_20210306_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritmusic',
            name='TimeFavorti',
            field=models.DateTimeField(default=datetime.time(18, 12, 59, 444185)),
        ),
    ]
