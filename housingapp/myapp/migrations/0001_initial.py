# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyAddress', models.CharField(max_length=200)),
                ('propertyDescription', models.CharField(max_length=250)),
                ('propertyNumRooms', models.IntegerField(default=0)),
                ('propertyNumBaths', models.IntegerField(default=0)),
                ('propertyNumPersons', models.IntegerField(default=0)),
                ('propertyAC', models.BooleanField(default=False)),
                ('propertyHeat', models.BooleanField(default=False)),
                ('propertyPorch', models.BooleanField(default=False)),
                ('propertyBackyard', models.BooleanField(default=False)),
                ('propertyWasherDryer', models.BooleanField(default=False)),
                ('propertyRating', models.IntegerField(default=0)),
                ('landlordRating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewPropertyRating', models.IntegerField(default=0)),
                ('reviewLandlordRating', models.IntegerField(default=0)),
                ('reviewProperty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Property')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('universityTag', models.CharField(max_length=100)),
                ('universityName', models.CharField(max_length=100)),
                ('universityTown', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='propertyUniversity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.University'),
        ),
    ]
