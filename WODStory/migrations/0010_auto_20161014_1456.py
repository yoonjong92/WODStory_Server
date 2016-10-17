# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0009_auto_20161014_1452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wod',
            old_name='rounds',
            new_name='round',
        ),
        migrations.AddField(
            model_name='wod',
            name='emomperminute',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='wod',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 10, 14, 14, 56, 2, 939974)),
        ),
    ]
