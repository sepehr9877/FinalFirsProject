# Generated by Django 3.1.6 on 2021-03-15 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0033_auto_20210315_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 15, 20, 7, 29, 509663)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='time_comments',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 15, 20, 7, 29, 509663)),
        ),
    ]
