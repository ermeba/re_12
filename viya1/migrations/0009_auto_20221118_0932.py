# Generated by Django 3.2.15 on 2022-11-18 06:32

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('viya1', '0008_auto_20221117_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='addressOf',
            field=models.CharField(default=datetime.datetime(2022, 11, 18, 6, 32, 14, 857045, tzinfo=utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 11, 18, 6, 32, 14, 855017, tzinfo=utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 11, 18, 6, 32, 14, 856048, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='division',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 11, 18, 6, 32, 14, 856048, tzinfo=utc), max_length=20),
        ),
        migrations.CreateModel(
            name='OfferProjectPhotosS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_project', models.ImageField(blank=True, null=True, upload_to='offers/')),
                ('offer_project_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OfferProject_OfferProjectPhotosS', to='viya1.offerproject')),
            ],
        ),
    ]
