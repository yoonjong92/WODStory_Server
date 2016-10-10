# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0003_auto_20161005_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wod',
            name='author',
            field=models.ForeignKey(related_name='wods', to=settings.AUTH_USER_MODEL),
        ),
    ]
