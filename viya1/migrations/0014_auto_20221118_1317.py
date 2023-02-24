# Generated by Django 3.2.15 on 2022-11-18 10:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('viya1', '0013_auto_20221118_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='addressOf',
            field=models.CharField(default=datetime.datetime(2022, 11, 18, 10, 17, 52, 627418, tzinfo=utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 11, 18, 10, 17, 52, 623418, tzinfo=utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 11, 18, 10, 17, 52, 625421, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='division',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 11, 18, 10, 17, 52, 624419, tzinfo=utc), max_length=20),
        ),
        migrations.AlterField(
            model_name='offerprojectphotoss',
            name='photo_project',
            field=models.ImageField(blank=True, null=True, upload_to='offerproject/'),
        ),
    ]
