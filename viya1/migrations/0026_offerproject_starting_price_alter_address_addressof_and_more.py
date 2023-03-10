# Generated by Django 4.1.7 on 2023-02-16 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viya1', '0025_auto_20221119_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerproject',
            name='starting_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='addressOf',
            field=models.CharField(default=datetime.datetime(2023, 2, 16, 18, 24, 38, 710664, tzinfo=datetime.timezone.utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default=datetime.datetime(2023, 2, 16, 18, 24, 38, 708669, tzinfo=datetime.timezone.utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(default=datetime.datetime(2023, 2, 16, 18, 24, 38, 709667, tzinfo=datetime.timezone.utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='division',
            name='name',
            field=models.CharField(default=datetime.datetime(2023, 2, 16, 18, 24, 38, 709667, tzinfo=datetime.timezone.utc), max_length=20),
        ),
    ]
