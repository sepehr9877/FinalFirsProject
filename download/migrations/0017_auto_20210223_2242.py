# Generated by Django 3.1.6 on 2021-02-23 19:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0016_auto_20210223_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloaddetail',
            name='recnetlydownload',
            field=models.TimeField(default=datetime.time(22, 42, 1, 329140)),
        ),
        migrations.AlterField(
            model_name='downloadsong',
            name='Download_Time',
            field=models.TimeField(default=datetime.time(22, 42, 1, 329140)),
        ),
    ]
