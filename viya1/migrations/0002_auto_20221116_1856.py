# Generated by Django 3.2.15 on 2022-11-16 15:56

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('viya1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerproject',
            name='district_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OfferProject_District', to='viya1.district'),
        ),
        migrations.AddField(
            model_name='offerproject',
            name='division_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OfferProject_Division', to='viya1.division'),
        ),
        migrations.AddField(
            model_name='offerproject',
            name='offers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OfferProject_OfferProjectPhotos', to='viya1.offerprojectphotos'),
        ),
        migrations.AddField(
            model_name='offerproject',
            name='offers_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OfferProject_OfferProjectPlanPhotos', to='viya1.offerprojectplanphotos'),
        ),
        migrations.AlterField(
            model_name='address',
            name='addressOf',
            field=models.CharField(default=datetime.datetime(2022, 11, 16, 15, 56, 20, 115316, tzinfo=utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 11, 16, 15, 56, 20, 113316, tzinfo=utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 11, 16, 15, 56, 20, 114317, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='division',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 11, 16, 15, 56, 20, 114317, tzinfo=utc), max_length=20),
        ),
    ]
