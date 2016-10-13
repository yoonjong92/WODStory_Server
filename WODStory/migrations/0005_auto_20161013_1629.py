# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0004_auto_20161013_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='distance_unit',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='workout',
            name='weight_unit',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
    ]
