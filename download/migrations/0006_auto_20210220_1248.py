# Generated by Django 3.1.6 on 2021-02-20 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0005_auto_20210216_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloaddetail',
            name='recnetlydownload',
            field=models.TimeField(default=datetime.time(12, 48, 29, 27247)),
        ),
        migrations.AlterField(
            model_name='downloadsong',
            name='Download_Time',
            field=models.TimeField(default=datetime.time(12, 48, 29, 27247)),
        ),
    ]
