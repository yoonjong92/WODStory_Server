# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wod',
            old_name='author',
            new_name='user',
        ),
    ]
