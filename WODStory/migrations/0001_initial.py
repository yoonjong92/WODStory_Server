# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='WOD',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('result_time', models.TimeField(blank=True, null=True)),
                ('result_rounds', models.IntegerField(blank=True, null=True)),
                ('result_reps', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WODType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('distance', models.IntegerField(blank=True, null=True)),
                ('reps', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], unique=True, max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', verbose_name='username', error_messages={'unique': 'A user with that username already exists.'})),
                ('first_name', models.CharField(blank=True, verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(blank=True, verbose_name='last name', max_length=30)),
                ('email', models.EmailField(blank=True, verbose_name='email address', max_length=254)),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('authtoken', models.CharField(blank=True, null=True, max_length=200)),
                ('groups', models.ManyToManyField(verbose_name='groups', related_name='user_set', related_query_name='user', blank=True, to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', related_name='user_set', related_query_name='user', blank=True, to='auth.Permission', help_text='Specific permissions for this user.')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='workout',
            name='name',
            field=models.ForeignKey(to='WODStory.WorkoutType', to_field='name'),
        ),
        migrations.AddField(
            model_name='workout',
            name='wod',
            field=models.ForeignKey(to='WODStory.WOD', related_name='workouts'),
        ),
        migrations.AddField(
            model_name='wod',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='wods'),
        ),
        migrations.AddField(
            model_name='wod',
            name='type',
            field=models.ForeignKey(to='WODStory.WODType', default=0),
        ),
    ]
