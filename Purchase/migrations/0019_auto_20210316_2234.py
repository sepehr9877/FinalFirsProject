# Generated by Django 3.1.6 on 2021-03-16 19:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Purchase', '0018_auto_20210316_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 22, 34, 0, 879049)),
        ),
    ]
