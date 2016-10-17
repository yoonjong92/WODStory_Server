# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0010_auto_20161014_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wod',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 10, 14, 14, 56, 31, 483314)),
        ),
    ]
