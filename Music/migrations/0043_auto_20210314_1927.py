# Generated by Django 3.1.6 on 2021-03-14 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0042_auto_20210314_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='time_add',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 14, 19, 27, 55, 752713)),
        ),
    ]
