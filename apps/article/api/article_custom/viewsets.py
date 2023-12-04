from django.db.models import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.article.models import Article

from .serializers import ArticleCustomSerializer


class ArticlesCustomViewSet(APIView, LimitOffsetPagination):
    serializer_class = ArticleCustomSerializer
    http_method_names = ['get', ]

    def get(self, request):
        author_id = self.request.GET.get('author_id')
        module_id = self.request.GET.get('module_id')
        category_id = self.request.GET.get('category_id')

        f = Q()

        if author_id is not None and author_id != '':
            f &= Q(author_id=author_id)
        if module_id is not None and module_id != '':
            f &= Q(module_id=module_id)
        if category_id is not None and category_id != '':
            f &= Q(category_id=category_id)

        queryset = Article.objects.filter(f)

        results = self.paginate_queryset(queryset, request, view=self)
        serializer = ArticleCustomSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
    
    

class ArticleCustomViewSet(APIView):
    serializer_class = ArticleCustomSerializer
    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        queryset = Article.objects.filter(id=kwargs.get('article_id'))
        serializer = ArticleCustomSerializer(queryset, many=True)
        return Response(serializer.data[0])
    
