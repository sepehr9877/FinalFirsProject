# Generated by Django 3.1.6 on 2021-03-02 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0016_auto_20210302_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='time_add',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 2, 12, 35, 20, 367581)),
        ),
    ]
