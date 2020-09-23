from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
