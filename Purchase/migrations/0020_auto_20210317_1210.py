# Generated by Django 3.1.6 on 2021-03-17 08:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Purchase', '0019_auto_20210316_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 17, 12, 10, 7, 329651)),
        ),
    ]
