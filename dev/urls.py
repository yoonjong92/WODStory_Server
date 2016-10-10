from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

urlpatterns = [
    # Examples:
    # url(r'^$', 'dev.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('WODStory.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
]
