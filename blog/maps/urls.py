import views
from django.conf.urls import patterns, include, url

urlpatterns = [
  url(r'^$', views.map_view, name='map_view'),
  url(r'^send_position/$', views.send_position, name='send_position'),
]
