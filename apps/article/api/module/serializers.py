from apps.article.models import Article, Category, Module
from django.contrib.auth.models import User
from django.db.models import Avg
from rest_framework import serializers


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = (
            'id',
            'module',
            'active',
        )

