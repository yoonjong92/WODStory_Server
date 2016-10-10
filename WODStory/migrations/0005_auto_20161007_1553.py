# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WODStory', '0004_auto_20161007_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='WODType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('weight', models.IntegerField(null=True)),
                ('distance', models.IntegerField(null=True)),
                ('reps', models.IntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='wod',
            name='published_date',
        ),
        migrations.AddField(
            model_name='wod',
            name='result_reps',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='wod',
            name='result_rounds',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='wod',
            name='result_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='wod',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='workout',
            name='wod',
            field=models.ForeignKey(related_name='workouts', to='WODStory.WOD'),
        ),
        migrations.AddField(
            model_name='wod',
            name='type',
            field=models.ForeignKey(default=0, to='WODStory.WODType'),
        ),
    ]
