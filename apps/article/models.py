from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    class Meta:
        abstract = True


class Module(Base):
    module = models.CharField(max_length=255, unique=True)


    class Meta:
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'
        ordering = ['id']

    def __str__(self):
        return self.module


class Category(Base):
    name = models.CharField(max_length=255, unique=True)
    module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(Base):
    title = models.CharField(max_length=255, unique=True)
    image = models.URLField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    text = models.TextField()
    published = models.BooleanField(default=False)
    module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['id']

    def __str__(self):
        return self.title


class Evaluation(Base):
    comment = models.TextField(blank=True, default='')
    evaluation = models.DecimalField(max_digits=2, decimal_places=1)
    article = models.ForeignKey(Article, related_name='evaluations', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    class Meta:
        verbose_name = 'Evaluation'
        verbose_name_plural = 'Evaluations'
        ordering = ['id']
        unique_together = ['user', 'article']

    def __str__(self):
        return f'{self.user.username} avaliou o article {self.article} com nota de {self.evaluation}'
