from django.contrib import admin
from .models import WOD, WODType, Workout, WorkoutType

# Register your models here.

admin.site.register(WOD)
admin.site.register(WODType)
admin.site.register(Workout)
admin.site.register(WorkoutType)
