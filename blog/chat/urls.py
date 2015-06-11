import views
from django.conf.urls import patterns, include, url

#url(r'^$', views.home_chat, name='home_chat'),
#url(r'^process/$', views.process_message, name='process_message'),

urlpatterns = [
  url(r'^$', views.home_chat, name='home_chat'),
  url(r'^process/$', views.process_message, name='process_message'),
  url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}, name='login'),
  url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
]
