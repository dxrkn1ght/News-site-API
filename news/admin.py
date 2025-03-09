from django.contrib import admin
from .models import New


@admin.register(New)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'image','is_published')
    search_fields = ('is_published', 'category', )
    list_filter = ('created_at',)
    ordering = ('created_at',)

# category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news')
# tags = models.ManyToManyField(Tag, related_name='news')
# image = models.ImageField(null=True)
# views_count = models.PositiveIntegerField(default=0)
# is_published = models.BooleanField(default=False)
# created_at = models.DateTimeField(auto_now_add=True)
# updated_at = models.DateTimeField(auto_now=True)
