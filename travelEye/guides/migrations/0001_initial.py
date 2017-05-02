# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-30 09:14
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PointsOfInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'PointsOfInterest',
            },
        ),
        migrations.CreateModel(
            name='Streets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('location', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Streets',
            },
        ),
    ]
