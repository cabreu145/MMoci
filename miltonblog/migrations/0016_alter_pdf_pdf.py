# Generated by Django 3.2 on 2021-04-27 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miltonblog', '0015_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='pdf',
            field=models.FileField(blank=True, upload_to='pdf/', verbose_name='Sonrisas PDF'),
        ),
    ]
