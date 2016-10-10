# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0005_auto_20161007_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wod',
            name='result_reps',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wod',
            name='result_rounds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wod',
            name='result_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='distance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
