# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='reviewDescription',
            field=models.CharField(default=b'', max_length=1000),
        ),
        migrations.AlterField(
            model_name='property',
            name='landlordRating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='property',
            name='propertyRating',
            field=models.FloatField(default=0.0),
        ),
    ]
