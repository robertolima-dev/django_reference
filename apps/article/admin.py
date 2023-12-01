from django.contrib import admin

from .models import Article, Category, Evaluation, Module

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Module, ModuleAdmin)