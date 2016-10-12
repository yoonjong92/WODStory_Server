# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0002_auto_20161011_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='reps',
            field=models.TextField(),
        ),
    ]
