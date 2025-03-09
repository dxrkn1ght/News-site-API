from django.contrib import admin
from .models import New


@admin.register(New)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'image','is_published')
    search_fields = ('is_published', 'category', )
    list_filter = ('created_at',)
    ordering = ('created_at',)

