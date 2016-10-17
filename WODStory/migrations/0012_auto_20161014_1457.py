# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0011_auto_20161014_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wod',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
