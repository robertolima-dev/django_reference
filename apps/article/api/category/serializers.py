from apps.article.api.module.serializers import ModuleSerializer
from apps.article.models import Article, Category, Module
from django.contrib.auth.models import User
from django.db.models import Avg
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'module',
            'active',
        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['module'] = ModuleSerializer(instance.module).data
        return response