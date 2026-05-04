from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("titre", "categorie", "date_publication", "publie")
    list_filter = ("categorie", "publie")
    search_fields = ("titre",)
    prepopulated_fields = {"slug": ("titre",)}
