from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'new', 'author_name', 'author_email', 'content','is_approved')
    search_fields = ('author_name', 'author_email', 'content')
    list_filter = ('created_at',)
    ordering = ('created_at',)

