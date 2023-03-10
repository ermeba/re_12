# Generated by Django 3.2.15 on 2022-11-19 05:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('viya1', '0020_auto_20221119_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='addressOf',
            field=models.CharField(default=datetime.datetime(2022, 11, 19, 5, 4, 35, 81992, tzinfo=utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 11, 19, 5, 4, 35, 79993, tzinfo=utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 11, 19, 5, 4, 35, 80993, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='division',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 11, 19, 5, 4, 35, 79993, tzinfo=utc), max_length=20),
        ),
        migrations.CreateModel(
            name='OfferProjectMapsS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('km', models.CharField(blank=True, max_length=100, null=True)),
                ('place', models.CharField(blank=True, max_length=100, null=True)),
                ('place_name', models.CharField(blank=True, max_length=100, null=True)),
                ('links', models.URLField(blank=True, max_length=400, null=True)),
                ('offer_project_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OfferProject_OfferProjectMapsS', to='viya1.offerproject')),
            ],
        ),
    ]
