# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0015_auto_20161017_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wod',
            name='emomminute',
            field=models.IntegerField(null=True, blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='wod',
            name='emomperminute',
            field=models.IntegerField(null=True, blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='wod',
            name='round',
            field=models.IntegerField(null=True, blank=True, default=1),
        ),
    ]
