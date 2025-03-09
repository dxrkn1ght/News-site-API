from django.contrib import admin
from .models import New


@admin.register(New)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','slug')
    search_fields = ('name', )
    list_filter = ('name',)
    ordering = ('name',)

