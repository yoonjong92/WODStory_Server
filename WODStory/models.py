from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    authtoken = models.CharField(max_length=200,null=True,blank=True)

class WODType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class WOD(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="wods")
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField(default=timezone.datetime.today())
    type = models.ForeignKey('WODType', default = 0)
    rounds = models.IntegerField(default = 1, null=True)
    emomminute = models.IntegerField(default = 1, null=True)
    result_time = models.TimeField(blank=True,null=True)
    result_rounds = models.IntegerField(blank=True, null=True)
    result_reps = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

class WorkoutType(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Workout(models.Model):
    wod = models.ForeignKey('WOD', related_name="workouts")
    name = models.ForeignKey('WorkoutType', to_field='name',validators=[])
    weight = models.IntegerField(blank=True,null = True)
    weight_unit = models.CharField(max_length = 100, blank=True,null = True)
    distance = models.IntegerField(blank=True,null = True)
    distance_unit = models.CharField(max_length = 100, blank=True,null = True)
    reps = models.TextField()

    def __str__(self):
        return self.id
