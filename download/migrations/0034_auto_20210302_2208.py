# Generated by Django 3.1.6 on 2021-03-02 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0033_auto_20210302_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloaddetail',
            name='recnetlydownload',
            field=models.TimeField(default=datetime.time(22, 8, 37, 870741)),
        ),
        migrations.AlterField(
            model_name='downloadsong',
            name='Download_Time',
            field=models.TimeField(default=datetime.time(22, 8, 37, 870741)),
        ),
    ]
