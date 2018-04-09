from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^test/$', views.pagetest, name='pagetest'),
    url(r'^$', views.index, name='index'),
]