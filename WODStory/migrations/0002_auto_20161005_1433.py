# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailywod',
            name='created_date',
        ),
        migrations.AddField(
            model_name='dailywod',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
