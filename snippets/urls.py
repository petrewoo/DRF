#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.conf.urls import url
from snippets import views

urlpatterns = [
    url('^snippets/$', views.snippet_list),
    url('^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail)
]
