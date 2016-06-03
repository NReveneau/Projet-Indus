# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin

from balafon.urls import urlpatterns

balafon_urlpatterns = urlpatterns

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('eleve.urls'))
]

urlpatterns += balafon_urlpatterns
