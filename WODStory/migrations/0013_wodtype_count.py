# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0012_auto_20161014_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='wodtype',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
