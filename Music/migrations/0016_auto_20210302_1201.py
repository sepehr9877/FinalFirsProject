# Generated by Django 3.1.6 on 2021-03-02 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0015_auto_20210302_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='time_add',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 2, 12, 1, 17, 192208)),
        ),
    ]
