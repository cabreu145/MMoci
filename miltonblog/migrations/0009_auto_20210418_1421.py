# Generated by Django 3.2 on 2021-04-18 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miltonblog', '0008_auto_20210418_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postvideo',
            name='mp4',
        ),
        migrations.RemoveField(
            model_name='postvideo',
            name='webm',
        ),
    ]
