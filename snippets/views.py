# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

from rest_framework import mixins
from rest_framework import generics

# Create your views here.


class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, reqeust, *args, **kwargs):
        return self.list(reqeust, *args, **kwargs)

    def post(self, reqeust, *args, **kwargs):
        return self.create(reqeust, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
