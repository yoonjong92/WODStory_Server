from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from WODStory.views import wodviews
from WODStory.views import userviews

urlpatterns = [
    url(r'^wods/$', wodviews.WODSList.as_view(), name="wod-list"),
    url(r'^wods/(?P<pk>[0-9]+)/$', wodviews.WODDetail.as_view(), name="wod-detail"),
    url(r'^signin/$', userviews.AuthwithToken.as_view(), name="user-auth"),
    url(r'^users/$', userviews.UserList.as_view(), name="user-list"),
    url(r'^users/(?P<pk>[0-9]+)/$', userviews.UserDetail.as_view(), name="user-detail"),
    url(r'^workout/$', wodviews.WorkoutList.as_view(), name="workout-list"),
    url(r'^workouttype/$', wodviews.WorkoutTypeList.as_view(), name="workouttype-list"),
    url(r'^wodsearch/$', wodviews.WODSearch.as_view(), name="wod-search"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
