from django.http.response import HttpResponse
from django.shortcuts import render
from WODStory.models import DailyWOD
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView

# Create your views here.

def dailyWOD_list(request):
    dailyWOD_list = DailyWOD.objects.all()

    return HttpResponse(dailyWOD_list[0].title)

class DailyWODSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyWOD

class api_dailyWODList(GenericAPIView, mixins.ListModelMixin):
    queryset = DailyWOD.objects.all()
    serializer_class = DailyWODSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
