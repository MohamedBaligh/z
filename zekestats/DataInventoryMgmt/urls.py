# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^category$', views.showcategory, name='category'),
    url(r'^datasets/(?P<category>\w+)/$', views.datasets, name='dataset'),
    url(r'^datainfo/(?P<info>[-\w]+)/$', views.datainfo, name='datainfo'),
]
