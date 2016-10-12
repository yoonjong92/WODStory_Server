from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import WOD, WODType, Workout, WorkoutType

# Register your models here.

admin.site.register(get_user_model())
admin.site.register(WOD)
admin.site.register(WODType)
admin.site.register(Workout)
admin.site.register(WorkoutType)
