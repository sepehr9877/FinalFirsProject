# Generated by Django 3.1.6 on 2021-03-02 08:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0022_auto_20210228_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloaddetail',
            name='recnetlydownload',
            field=models.TimeField(default=datetime.time(11, 45, 10, 635619)),
        ),
        migrations.AlterField(
            model_name='downloadsong',
            name='Download_Time',
            field=models.TimeField(default=datetime.time(11, 45, 10, 635619)),
        ),
    ]
