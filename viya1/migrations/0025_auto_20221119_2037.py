# Generated by Django 3.2.15 on 2022-11-19 17:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('viya1', '0024_auto_20221119_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='addressOf',
            field=models.CharField(default=datetime.datetime(2022, 11, 19, 17, 37, 51, 326991, tzinfo=utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 11, 19, 17, 37, 51, 323992, tzinfo=utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 11, 19, 17, 37, 51, 324992, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='division',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 11, 19, 17, 37, 51, 324992, tzinfo=utc), max_length=20),
        ),
        migrations.AlterField(
            model_name='offerprojectroomtype',
            name='price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='offerprojectroomtype',
            name='square_meter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
