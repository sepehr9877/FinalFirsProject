# Generated by Django 3.1.6 on 2021-03-15 18:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Purchase', '0014_auto_20210315_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 15, 22, 4, 4, 885170)),
        ),
    ]
