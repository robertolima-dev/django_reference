from django.contrib.auth.models import User
from django.db.models import Avg
from rest_framework import serializers

from apps.article.api.category.serializers import CategorySerializer
# from apps.article.api.evaluation.serializers import EvaluationSerializer
from apps.article.api.module.serializers import ModuleSerializer
from apps.article.models import Article, Category, Module


class CurrentUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username', 
            'email', 
            )


class ArticleSerializer(serializers.ModelSerializer):

    # evaluations = EvaluationSerializer(many=True, read_only=True)
    # evaluations = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='evaluation-detail')

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'image',
            'slug',
            'text',
            'published',
            'module',
            'category',
            'author',
            # 'evaluations',
            'created_at',
            'updated_at',
            'active',
        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['author'] = CurrentUserSerializer(instance.author).data
        response['category'] = CategorySerializer(instance.category).data
        response['module'] = ModuleSerializer(instance.module).data
        return response
