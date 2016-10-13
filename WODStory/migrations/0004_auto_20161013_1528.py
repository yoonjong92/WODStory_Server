# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0003_auto_20161012_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='wod',
            name='emomminute',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='wod',
            name='rounds',
            field=models.IntegerField(default=1),
        ),
    ]
