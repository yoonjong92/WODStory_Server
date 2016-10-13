# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0006_auto_20161013_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wod',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 10, 13, 17, 30, 12, 574594)),
        ),
    ]
