from django.contrib import admin
from .models import Category

@admin.register(Category)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'slug' )
    search_fields = ('name', 'description', 'slug')
    list_filter = ('created_at',)
    ordering = ('name',)

