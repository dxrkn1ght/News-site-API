from rest_framework import serializers
from django.utils.text import slugify
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        extra_kwargs = {
            'slug': {'read_only': True}
        }


