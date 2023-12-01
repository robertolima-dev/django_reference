from apps.article.models import Module
from rest_framework import viewsets

from .serializers import ModuleSerializer

# Create your views here.

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer