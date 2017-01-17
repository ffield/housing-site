from django.conf.urls import url
from myapp import views



urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^logout/$', views.logout, name = 'logout'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^(?P<universityTag>[\w\-]+)/$', views.college, name='college'),
    url(r'^(?P<universityTag>[\w\-]+)/(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<universityTag>[\w\-]+)/(?P<id>[0-9]+)/review$', views.rate, name='rateProperty')
]