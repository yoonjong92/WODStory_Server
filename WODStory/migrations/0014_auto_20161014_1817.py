# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0013_wodtype_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wodtype',
            name='count',
        ),
        migrations.AddField(
            model_name='workouttype',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
