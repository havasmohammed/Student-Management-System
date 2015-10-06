from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.loginpage, name='loginpage'),
    # url(r'^/basicdetail/$', views.Basic_detail, name='basicdetail')
]
