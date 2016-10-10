from django.db import models
from django.utils import timezone

# Create your models here.

class WODType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class WOD(models.Model):
    author = models.ForeignKey('auth.User', related_name="wods")
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField(default=timezone.now)
    type = models.ForeignKey('WODType', default = 0)
    result_time = models.TimeField(blank=True,null=True)
    result_rounds = models.IntegerField(blank=True, null=True)
    result_reps = models.IntegerField(blank=True, null=True)

#    def __str__(self):
#        return self.title

class WorkoutType(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Workout(models.Model):
    wod = models.ForeignKey('WOD', related_name="workouts")
    name = models.ForeignKey('WorkoutType', to_field='name',validators=[])
    weight = models.IntegerField(blank=True,null = True)
    distance = models.IntegerField(blank=True,null = True)
    reps = models.IntegerField(default = 1)

    def __str__(self):
        return self.id
