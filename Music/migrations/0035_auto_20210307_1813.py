# Generated by Django 3.1.6 on 2021-03-07 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0034_auto_20210306_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='time_add',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 7, 18, 12, 59, 443188)),
        ),
    ]
