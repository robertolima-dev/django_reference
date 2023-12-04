from django.conf import settings
from rest_framework import serializers

from apps.article.api.article.serializers import CurrentUserSerializer
from apps.article.api.evaluation.serializers import EvaluationObjSerializer


class ArticleCustomSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=254)
    image = serializers.CharField(max_length=254)
    slug = serializers.CharField(max_length=254)
    text = serializers.CharField(max_length=5000)
    published = serializers.BooleanField(default=False)
    author = CurrentUserSerializer(many=False, read_only=True)
    evaluations = EvaluationObjSerializer(many=True, read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    active = serializers.BooleanField(default=True)

    category_name = serializers.CharField(source='category.name', read_only=True)
    module_name = serializers.CharField(source='module.module', read_only=True)

