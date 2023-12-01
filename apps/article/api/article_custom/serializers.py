from django.conf import settings
from rest_framework import serializers

from apps.article.api.article.serializers import CurrentUserSerializer
from apps.article.api.category.serializers import CategorySerializer
from apps.article.api.evaluation.serializers import EvaluationObjSerializer
from apps.article.api.module.serializers import ModuleSerializer


class ArticleCustomSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    title = serializers.CharField(max_length=254)
    image = serializers.CharField(max_length=254)
    slug = serializers.CharField(max_length=254)
    text = serializers.CharField(max_length=5000)
    published = serializers.BooleanField(default=False)
    module = ModuleSerializer(many=False)
    category = CategorySerializer(many=False)
    author = CurrentUserSerializer(many=False)
    evaluations = EvaluationObjSerializer(many=True)
    updated_at = serializers.DateTimeField()
    created_at = serializers.DateTimeField()
    active = serializers.BooleanField(default=False)