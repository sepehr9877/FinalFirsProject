# Generated by Django 3.1.6 on 2021-02-21 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserPlayList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_playlist',
            name='PlayListName',
            field=models.CharField(default='Name', max_length=150),
        ),
    ]
