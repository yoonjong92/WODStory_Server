# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0008_auto_20161014_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workout',
            old_name='reps',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='distance',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='distance_unit',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='time',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='time_unit',
        ),
        migrations.AlterField(
            model_name='wod',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 10, 14, 14, 52, 9, 937143)),
        ),
    ]
