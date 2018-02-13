#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    url('^snippets/$', views.snippet_list),
    url('^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
