from django.contrib.auth.models import User
from django.db.models import Avg
from rest_framework import serializers

from apps.article.api.article.serializers import (ArticleSerializer,
                                                  CurrentUserSerializer)
from apps.article.models import Evaluation


class EvaluationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Evaluation
        fields = (
            'id',
            'comment',
            'evaluation',
            'user',
            'article',
            'created_at',
            'updated_at',
            'active',
        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = CurrentUserSerializer(instance.user).data
        response['article'] = ArticleSerializer(instance.article).data
        return response
    

class EvaluationObjSerializer(serializers.ModelSerializer):


    class Meta:
        model = Evaluation
        fields = (
            'id',
            'comment',
            'evaluation',
            'user',
            'created_at',
            'updated_at',
            'active',
        )
