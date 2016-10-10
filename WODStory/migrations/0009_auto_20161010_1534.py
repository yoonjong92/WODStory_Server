# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0008_auto_20161007_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='name',
            field=models.ForeignKey(to='WODStory.WorkoutType', to_field='name'),
        ),
    ]
