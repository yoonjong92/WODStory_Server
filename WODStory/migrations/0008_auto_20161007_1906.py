# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0007_auto_20161007_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='name',
            field=models.ForeignKey(to_field='name', to='WODStory.WorkoutType', db_constraint=False),
        ),
    ]
