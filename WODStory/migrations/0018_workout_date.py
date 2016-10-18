# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0017_workout_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
