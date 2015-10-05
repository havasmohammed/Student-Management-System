from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Basic_detail, name='Basic_detail'),
]
