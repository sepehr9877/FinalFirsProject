# Generated by Django 3.1.6 on 2021-03-16 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20210315_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='accept_by_user',
            field=models.BooleanField(default=False),
        ),
    ]
