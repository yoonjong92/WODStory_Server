# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0007_auto_20161013_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='time_unit',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='wod',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 10, 14, 14, 51, 49, 965868)),
        ),
    ]
