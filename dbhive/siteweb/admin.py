from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'publie', 'date_publication')
    list_filter = ('publie', 'categorie')
    prepopulated_fields = {"slug": ("titre",)}
