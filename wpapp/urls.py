from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<station_id>[0-9]+)/$', views.wplots, name='wplots'),
]
