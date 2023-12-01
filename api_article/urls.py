"""
URL configuration for api_article project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from apps.article.api.article.viewsets import ArticleViewSet
from apps.article.api.article_custom.viewsets import ArticleCustomViewSet
from apps.article.api.category.viewsets import CategoryViewSet
from apps.article.api.evaluation.viewsets import EvaluationViewSet
from apps.article.api.module.viewsets import ModuleViewSet

route_api_v1 = routers.DefaultRouter()
route_api_v1.register(r'articles', ArticleViewSet, basename='articles') # noqa E501
route_api_v1.register(r'categories', CategoryViewSet, basename='categories') # noqa E501
route_api_v1.register(r'modules', ModuleViewSet, basename='modules') # noqa E501
route_api_v1.register(r'evaluations', EvaluationViewSet, basename='evaluations') # noqa E501

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/custom/', ArticleCustomViewSet.as_view(), name='custom'),
]

urlpatterns.append(
    path('api/v1/', include(route_api_v1.urls)),
)