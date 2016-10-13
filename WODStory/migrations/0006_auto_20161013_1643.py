# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0005_auto_20161013_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wod',
            name='emomminute',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='wod',
            name='rounds',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
