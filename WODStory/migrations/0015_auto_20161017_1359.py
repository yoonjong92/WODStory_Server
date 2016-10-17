# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0014_auto_20161014_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wod',
            name='result_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
