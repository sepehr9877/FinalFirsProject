# Generated by Django 3.1.6 on 2021-03-17 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0043_auto_20210317_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 17, 20, 10, 24, 961503)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='time_comments',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 17, 20, 10, 24, 961503)),
        ),
    ]
