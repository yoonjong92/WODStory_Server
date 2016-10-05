from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dailyWOD/', views.dailyWOD_list, name='dailyWOD_list'),
    url(r'^api/dailyWOD/', views.api_dailyWODList.as_view(), name='api_dailyWODList'),
]
