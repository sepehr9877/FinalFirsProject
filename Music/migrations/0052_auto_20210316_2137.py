# Generated by Django 3.1.6 on 2021-03-16 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0051_auto_20210316_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='time_add',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 21, 37, 24, 91392)),
        ),
    ]
