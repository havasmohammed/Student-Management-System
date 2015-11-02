from django.conf.urls import url
# from django.contrib import admin

# from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^loginpage/$', views.loginpage, name='loginpage'),
    url(r'^loginpage/basicdetail/$', views.basicdetail, name='basicdetail')
]
