# Generated by Django 3.1.6 on 2021-03-16 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0050_auto_20210315_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='time_add',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 20, 21, 41, 757210)),
        ),
    ]
