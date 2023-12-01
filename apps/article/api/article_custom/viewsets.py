from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, views
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from apps.article.models import Article

from .serializers import ArticleCustomSerializer

# Create your views here.

class ArticleCustomViewSet(generics.ListCreateAPIView, LimitOffsetPagination):
    queryset = Article.objects.all()
    serializer_class = ArticleCustomSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'title', 'module', 'category', 'author']
    search_fields = ['=module', '=category', '=author']


    def get_queryset(self):
        order = self.request.GET.get('order')
        if order:
            return self.queryset.all().order_by(order)
        return self.queryset.all()
