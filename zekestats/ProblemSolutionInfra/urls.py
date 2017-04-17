from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^problems$', views.showproblems, name='problems'),
    url(r'^solutions$', views.showsolutions, name='solutions'),
    url(r'^problem/(?P<slug>[-\w]+)/$', views.showproblem, name='problem'),
]

