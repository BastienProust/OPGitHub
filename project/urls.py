from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'welcome.views.index', name ='index'),
]
