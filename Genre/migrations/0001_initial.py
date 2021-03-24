# Generated by Django 3.1.6 on 2021-02-09 13:43

import Genre.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameGenre', models.CharField(default='Genre', max_length=150)),
                ('image', models.ImageField(null=True, upload_to=Genre.models.upload_image)),
            ],
        ),
    ]
