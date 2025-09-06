from django.contrib import admin
from .models import Category,News

# admin.site.register(Category)
# admin.site.register(News)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(News)
class NewAdmin(admin.ModelAdmin):
    list_display = ["title","slug","created_at","status"]
    list_filter = ["title","created_at","status"]
    prepopulated_fields = {"slug":("title",)}
    search_fields = ["title","slug"]