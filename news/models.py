from django.db import models
from categories.models import Category
from tags.models import Tag
from django.utils.text import slugify


class New(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news')
    tags = models.ManyToManyField(Tag, related_name='news')
    image = models.ImageField(null=True)
    views_count = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(New, self).save(*args, **kwargs)

    def __str__(self):
        return self.title