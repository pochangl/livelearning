'''
Created on Jan 28, 2016

@author: streamer
'''
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^reverse', views.reverse_view),
    url(r'^param$', views.param, {"key1": 'key2'}),
    url(r'^user/12$', views.param, {"user_id": "789"}, name="twelve"),
    url(r'^user/(?P<user_id>[0-9]{2})$', views.param, name="user_page"),
]