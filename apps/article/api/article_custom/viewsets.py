from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, views
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from apps.article.models import Article, Category, Module

from .serializers import ArticleCustomSerializer

# Create your views here.

# class ArticleCustomViewSet(
#     generics.ListAPIView, 
#     LimitOffsetPagination
#     ):
#     queryset = Article.objects.all()
#     serializer_class = ArticleCustomSerializer

#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     filterset_fields = ['id', 'title', 'module', 'category', 'author']
#     search_fields = ['=module', '=category', '=author']


#     def get_queryset(self):
#         order = self.request.GET.get('order')
#         if order:
#             return self.queryset.all().order_by(order)
#         return self.queryset.all().order_by('-id')



class ArticlesCustomViewSet(
    views.APIView,
    LimitOffsetPagination
    ):
    serializer_class = ArticleCustomSerializer
    http_method_names = ['get', ]


    def get(self, request, *args, **kwargs):
        author_id = self.request.GET.get('author_id')
        if author_id is not None and author_id != '':
            queryset = Article.objects.filter(author_id=author_id)
        else:
            queryset = Article.objects.all()
        results = self.paginate_queryset(queryset, request, view=self)
        serializer = ArticleCustomSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
    

class ArticleCustomViewSet(
    views.APIView
    ):
    serializer_class = ArticleCustomSerializer
    http_method_names = ['get', ]


    def get(self, request, *args, **kwargs):
        queryset = Article.objects.filter(id=kwargs.get('article_id'))
        serializer = ArticleCustomSerializer(queryset, many=True)
        return Response(serializer.data[0])
    
