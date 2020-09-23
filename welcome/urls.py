from django.conf.urls import include, url

from . import views

urlpatterns = [
     url(r'^/', include(view.index, name='index')),
]
