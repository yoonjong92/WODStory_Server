# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0006_auto_20161007_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='workout',
            name='name',
            field=models.ForeignKey(to_field='name', to='WODStory.WorkoutType'),
        ),
    ]
