from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from apps.article.managers.delete_article import DeleteArticle
from apps.article.managers.update_article import UpdateArticle
from apps.article.models import Article

from .serializers import ArticleSerializer

# Create your views here.

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'title', 'module', 'category']
    search_fields = ['=module', '=category']
    ordering_fields = ['name', 'id', 'created_at']
    ordering = ['id']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.published is True and instance.active is True:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response(
                data={'detail': 'Não encontrado!'},
                status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        manager = UpdateArticle()
        can_update = manager.permisson_update(
            user=request.user, 
            article=instance
            )

        if can_update is True:
            data = request.data
            if 'title'in data:
                instance.title = data['title']
            if 'image'in data:
                instance.image = data['image']
            if 'slug'in data:
                instance.slug = data['slug']
            if 'text'in data:
                instance.text = data['text']
            if 'published'in data:
                instance.published = data['published']

            if 'category_id'in data:
                instance.category_id = data['category_id']
            if 'module_id'in data:
                instance.module_id = data['module_id']

            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response(
                    data={'detail': 'Não encontrado!'},
                    status=status.HTTP_404_NOT_FOUND
                )

    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        manager = DeleteArticle()
        can_delete = manager.permisson_delete(
            user=request.user, 
            article=instance
            )

        if can_delete is True:
            instance.active = False
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response(
                    data={'detail': 'Não encontrado!'},
                    status=status.HTTP_404_NOT_FOUND
                )