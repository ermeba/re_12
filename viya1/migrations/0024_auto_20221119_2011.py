# Generated by Django 3.2.15 on 2022-11-19 17:11

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('viya1', '0023_auto_20221119_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerproject',
            name='google_maps_field',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='address',
            name='addressOf',
            field=models.CharField(default=datetime.datetime(2022, 11, 19, 17, 11, 24, 965484, tzinfo=utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 11, 19, 17, 11, 24, 963485, tzinfo=utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 11, 19, 17, 11, 24, 964485, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='division',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 11, 19, 17, 11, 24, 964485, tzinfo=utc), max_length=20),
        ),
        migrations.AlterField(
            model_name='offerproject',
            name='google_maps_link',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]
