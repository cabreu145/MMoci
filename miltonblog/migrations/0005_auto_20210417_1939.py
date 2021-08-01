# Generated by Django 3.2 on 2021-04-18 00:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('miltonblog', '0004_auto_20210417_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimage',
            name='place',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='Lugar'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postimage',
            name='date',
            field=models.DateTimeField(verbose_name='Fecha'),
        ),
    ]
