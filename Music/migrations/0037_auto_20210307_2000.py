# Generated by Django 3.1.6 on 2021-03-07 16:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0036_auto_20210307_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='time_add',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 7, 20, 0, 12, 152367)),
        ),
    ]
