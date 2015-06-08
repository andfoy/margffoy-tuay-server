import views
from django.conf.urls import patterns, include, url

urlpatterns = [
  url(r'^$', views.home_chat, name='home_chat'),
  url(r'^node_api$', views.node_api, name='node_api'),
  url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}, name='login'),
  url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
]
