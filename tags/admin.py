from django.contrib import admin
from .models import Tag


@admin.register(Tag)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','slug')
    search_fields = ('name', )
    list_filter = ('name',)
    ordering = ('name',)

