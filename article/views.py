from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404 
from .models import Article
from .models import Author
from .serializers import ArticleSerializer 
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

class ArticleView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




		
