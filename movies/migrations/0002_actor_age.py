# Generated by Django 3.2.8 on 2021-10-27 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='age',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Возраст'),
        ),
    ]
